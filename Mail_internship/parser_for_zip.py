#!/usr/local/python/python2.7/bin/python2.7
# coding: utf-8
import json, csv, gzip
from pymystem3 import Mystem

import time
start = time.time()

m = Mystem()
trash = set([' ','\n','.','!','?'])

data = open("data_enc.csv", "w")
file2read = "logs03.gz"
total_enc = 0
inf = 0

class Query:
    def __init__(self, json_object):
	self.text = json.loads(json_object)[u'query'].get('qnorm')
	self.answer = enc(json_object)
	self.parsed = mystem(self.text.encode('utf-8'))
	self.inf = 0
	if 'инф' in self.parsed:
            self.inf = 1
	

def enc (json_object):
    enc = 0
    clicks = json.loads(json_object)[u'clicks']
    for click in clicks:
	link = click.get("link")
	if ("wikipedia.org/wiki/" in link) or ("dic.academic.ru" in link):
	    enc = 1
	    global total_enc
	    total_enc += 1
	    break
    return enc

def mystem(query):
    """
    Preprocess queries.
    """
    query = query.strip()
    query_parsed = m.analyze(query)
    gr_info = ''
    for word in query_parsed:
        if 'analysis' in word.keys() and len(word['analysis']) != 0:
            gr = word['analysis'][0]['gr'].encode('utf-8')
            gr_info += gr + ' '
    return gr_info

def main (file2read):
    writer = csv.writer(data, delimiter = "\t", lineterminator='\n')
    writer.writerow(["class", "query", "query_parsed", "infinitive"])
    file = gzip.open(file2read)
    for line in file:
	q = Query(line.decode("utf-8"))
	if q.answer == 1:
            writer.writerow([q.answer, q.text.encode('utf-8'), q.parsed, q.inf])
    data.close()
    return

main(file2read)

print "Number of enc queries: " + total_enc
print "it took", time.time() - start, "seconds."
