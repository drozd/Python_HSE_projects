#!/usr/bin/python
#coding: utf-8

#  Author: Angela Chapman
#  Date: 8/6/2014
#
#  This file contains code to accompany the Kaggle tutorial
#  "Deep learning goes to the movies".  The code in this file
#  is for Part 1 of the tutorial on Natural Language Processing.
#
# *************************************** #

import os,sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from gensim.models import Word2Vec

argument = sys.argv[1]

model = Word2Vec.load(argument)
index2word_set = set(model.index2word)
num_features = 500


def makeFeatureVec(words, model, num_features):
    # Function to average all of the word vectors in a given
    # paragraph
    #
    # Pre-initialize an empty numpy array (for speed)
    featureVec = np.zeros((num_features,),dtype="float32")
    #
    nwords = 0.
    #
    # Index2word is a list that contains the names of the words in 
    # the model's vocabulary. Convert it to a set, for speed 
    #
    # Loop over each word in the review and, if it is in the model's
    # vocaublary, add its feature vector to the total
    for word in words:
	if word.decode('utf-8') in index2word_set:
	    nwords = nwords + 1.
            featureVec = np.add(featureVec,model[word.decode('utf-8')])
    # Divide the result by the number of words to get the average
    featureVec = np.divide(featureVec,nwords)
    return featureVec


def getAvgFeatureVecs(reviews, model, num_features):
    # Given a set of reviews (each one a list of words), calculate 
    # the average feature vector for each one and return a 2D numpy array 
    # 
    # Initialize a counter
    counter = 0.
    # 
    # Preallocate a 2D numpy array, for speed
    reviewFeatureVecs = np.zeros((len(reviews),num_features),dtype="float32")
    for review in reviews:
	if counter%1000. == 0.:
	    print "Review %d of %d" % (counter, len(reviews))
	reviewFeatureVecs[counter] = makeFeatureVec(review, model, num_features)
	counter = counter + 1.
    return reviewFeatureVecs


if __name__ == '__main__':
    train = pd.read_csv(os.path.join(os.path.dirname(__file__), '.', 'reviews_train.csv'), header=0, \
                    delimiter="\t", quoting=3)
    test = pd.read_csv(os.path.join(os.path.dirname(__file__), '.', 'reviews_test.csv'), header=0, delimiter="\t", \
                   quoting=3 )

    # Initialize an empty list to hold the clean reviews
    clean_train_reviews = []

    for i in xrange( 0,len(train["review"])):
	# If the index is evenly divisible by 1000, print a message
	if( (i+1)%1000 == 0 ):
	    print "Review %d of %d\n" % ( i+1, len(train["review"]))
	clean_train_reviews.append(train["review"][i].split())
	
    trainDataVecs = getAvgFeatureVecs(clean_train_reviews,model,num_features )

    # Create an empty list and append the clean reviews one by one
    clean_test_reviews = []

    print "Cleaning and parsing the test set movie reviews...\n"
    
    for i in xrange(0,len(test["review"])):
	# If the index is evenly divisible by 1000, print a message
	if( (i+1)%1000 == 0 ):
	    print "Review %d of %d\n" % ( i+1, len(test["review"]))
	clean_test_reviews.append(test["review"][i].split())

    testDataVecs = getAvgFeatureVecs( clean_test_reviews, model, num_features )

    aspects = set(['Food','Interior','Price','Whole','Service'])
    accuracy = []
    for aspect in aspects:
	print "Training the random forest for %s (this may take a while)..." % aspect

	# Initialize a Random Forest classifier with 100 trees
	forest = RandomForestClassifier(n_estimators = 100)

	# Fit the forest to the training set, using the bag of words as
	# features and the sentiment labels as the response variable
	#
	# This may take a few minutes to run
	#print "Fitting a random forest to labeled training data..."
	forest = forest.fit(trainDataVecs, train[aspect] )
    
	# Use the random forest to make sentiment label predictions
	#print "Predicting test labels..."
	result = forest.predict(testDataVecs)

	# Copy the results to a pandas dataframe with an "id" column and
	# a "sentiment" column
	output = pd.DataFrame( data={"id":test["id"], aspect:result} )
	predictions = output.to_dict()

	## Use pandas to write the comma-separated output file
	output.to_csv(os.path.join(os.path.dirname(__file__), '.', 'word2vec.csv'), index=False, quoting=3)
	print "Wrote results to word2vec.csv"

	correct = 0
	incorrect = 0
	for i in xrange(0,len(test["review"])):
	    if test[aspect][i] == predictions[aspect][i]:
		correct += 1
	    else:
		incorrect += 1
	print correct,'predictions out of total',correct+incorrect
	total = (float(correct)/(correct+incorrect))*100
	print total,'% accuracy for', aspect,'\n'
	accuracy.append(total)
    print accuracy
    overall = np.mean(accuracy)
    print 'Overall accuracy:',overall