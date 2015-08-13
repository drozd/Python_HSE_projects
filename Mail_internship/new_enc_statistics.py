
# coding: utf-8

import json, csv, gzip
##from pymystem3 import Mystem

import time
start = time.time()

##m = Mystem()
##trash = set([' ','\n','.','!','?'])

data = open("data_enc.csv", "w")
file2read = "logs03.gz"
##inf = 0

class Query:
    def __init__(self, json_object):
	self.text = json.loads(json_object)[u'query'].get('qnorm')
	self.answer = enc(json_object)
##	self.parsed = mystem(self.text.encode('utf-8'))
##	self.inf = 0
##	if 'инф' in self.parsed:
##            self.inf = 1
	

def enc (json_object):
    enc = 0
    clicks = json.loads(json_object)[u'clicks']
    for click in clicks:
	link = click.get("link")
	if ("wikipedia.org/wiki/" in link) or ("dic.academic.ru" in link):
	    enc = 1
	    break
    return enc

##def mystem(query):
##    """
##    Preprocess queries.
##    """
##    query = query.strip()
##    query_parsed = m.analyze(query)
##    gr_info = ''
##    for word in query_parsed:
##        if 'analysis' in word.keys() and len(word['analysis']) != 0:
##            gr = word['analysis'][0]['gr'].encode('utf-8')
##            gr_info += gr + ' '
##    return gr_info


def main (file2read):
    dic = {}
    writer = csv.writer(data, delimiter = "\t", lineterminator='\n')
    writer.writerow(["query", "class", "wiki_clicks", "other_clicks", "score"])
    file = gzip.open(file2read)
    for line in file:
        q = Query(line.decode("utf-8"))
        key = str(q.text.encode('utf-8'))
        if key not in dic.keys():
            dic[key] = {'wiki_click' : 0, 'other' : 1}
        if q.answer == 1:
            dic[key]['wiki_click'] += 1
        else:
            dic[key]['other'] += 1
        if len(dic) % 10000 == 0:
            print "10,000!"
##        writer.writerow([q.answer, q.text.encode('utf-8')])

    for key in dic.keys():
        score = dic[key]['wiki_clicks'] / dic[key]['other']
        writer.writerow([q.text.encode('utf-8'), q.answer,
                         dic[key]['wiki_clicks'], dic[key]['other_clicks'],
                         score])
    data.close()
    return

main(file2read)

print "it took", time.time() - start, "seconds."
