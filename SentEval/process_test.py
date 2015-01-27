#!/usr/bin/python
# coding: utf-8
import sys
from xml.dom import minidom
from analyzer import sentiment

argument = sys.argv[1]

doc = minidom.parse(argument)
node = doc.documentElement
reviews = doc.getElementsByTagName("review")
for review in reviews:
    texts = review.getElementsByTagName("text")
    for text in texts:
	marks = sentiment(text.childNodes[-1].data)

    categories = review.getElementsByTagName("categories")
    for category in categories:
	cats = category.getElementsByTagName('category')
	for cat in cats:
	    cat_name = cat.getAttributeNode('name')
	    cat_sentiment = marks[cat_name.nodeValue.lower()]
	    cat.setAttribute('sentiment',cat_sentiment)

    print review.toxml(encoding='utf-8')