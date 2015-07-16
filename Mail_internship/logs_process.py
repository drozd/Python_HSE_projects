#!/usr/bin/python
# Processing search logs
# coding: utf-8

import sys,json

for line in sys.stdin:
    try:
	session = json.loads(line)
	query = session['query']
	urls = session['urls']
	clicks = session['clicks']
	print '====='
	print query["qnorm"]+'\t'+str(query["age"])+'\t'+str(query["sex"])+'\t'+query["time"]
	for url in clicks:
	    print url["link"]+'\t'+url["time"]
    except ValueError:
	print "Error!"
	print line
