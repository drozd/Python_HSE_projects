#!/usr/bin/python

#  Author: Angela Chapman
#  Date: 8/6/2014
#
#  This file contains code to accompany the Kaggle tutorial
#  "Deep learning goes to the movies".  The code in this file
#  is for Part 1 of the tutorial on Natural Language Processing.
#
# *************************************** #

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

if __name__ == '__main__':
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), '.', 'reviews_train.csv'), header=0, \
                    delimiter="\t", quoting=3)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), '.', 'reviews_test.csv'), header=0, delimiter="\t", \
                   quoting=3 )

    # Initialize an empty list to hold the clean reviews
    clean_train_reviews = []

    # Loop over each review; create an index i that goes from 0 to the length
    # of the movie review list

    print "Cleaning and parsing the training set movie reviews...\n"

    for i in xrange( 0,len(train["review"])):
	# If the index is evenly divisible by 1000, print a message
	if( (i+1)%1000 == 0 ):
	    print "Review %d of %d\n" % ( i+1, len(train["review"]))
	clean_train_reviews.append(train["review"][i])

    # ****** Create a bag of words from the training set
    #
    print "Creating the bag of words...\n"

    # Initialize the "CountVectorizer" object, which is scikit-learn's
    # bag of words tool.
    vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 5000)

    # fit_transform() does two functions: First, it fits the model
    # and learns the vocabulary; second, it transforms our training data
    # into feature vectors. The input to fit_transform should be a list of
    # strings.
    train_data_features = vectorizer.fit_transform(clean_train_reviews)

    # Numpy arrays are easy to work with, so convert the result to an
    # array
    train_data_features = train_data_features.toarray()


    # Create an empty list and append the clean reviews one by one
    clean_test_reviews = []

    #print "Cleaning and parsing the test set movie reviews...\n"
    
    for i in xrange(0,len(test["review"])):
	# If the index is evenly divisible by 1000, print a message
	if( (i+1)%1000 == 0 ):
	    print "Review %d of %d\n" % ( i+1, len(test["review"]))
	clean_test_reviews.append(test["review"][i])

    # Get a bag of words for the test set, and convert to a numpy array
    test_data_features = vectorizer.transform(clean_test_reviews)
    test_data_features = test_data_features.toarray()

    aspects = set(['Food','Interior','Price','Whole','Service'])
    accuracy = []
    for aspect in aspects:
	# ******* Train a random forest using the bag of words
	print "Training the random forest for %s (this may take a while)..." % aspect

	# Initialize a Random Forest classifier with 100 trees
	forest = RandomForestClassifier(n_estimators = 100)

	# Fit the forest to the training set, using the bag of words as
	# features and the sentiment labels as the response variable
	#
	# This may take a few minutes to run
	forest = forest.fit( train_data_features, train[aspect] )

	# Use the random forest to make sentiment label predictions
	print "Predicting test labels..."
	result = forest.predict(test_data_features)

	# Copy the results to a pandas dataframe with an "id" column and
	# a "sentiment" column
	output = pd.DataFrame( data={"id":test["id"], aspect:result} )
	predictions = output.to_dict()

	# Use pandas to write the comma-separated output file
	output.to_csv(os.path.join(os.path.dirname(__file__), '.', 'bow.csv'), index=False, quoting=3)
	print "Wrote results to bow.csv"

        correct = 0
        incorrect = 0
        for i in xrange(0,len(test["review"])):
            if test[aspect][i] == predictions[aspect][i]:
                correct += 1
            else:
                incorrect += 1
        print correct,'correct predictions out of total',correct+incorrect
        total = (float(correct)/(correct+incorrect))*100
        print total,'% accuracy for', aspect,'\n'
        accuracy.append(total)
    overall = np.mean(accuracy)
    print 'Overall accuracy:',overall