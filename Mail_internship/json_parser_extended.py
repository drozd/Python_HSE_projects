# -*- coding: utf-8 -*-

import json, csv, os
from pymystem3 import Mystem
import time
start = time.time()

m = Mystem()
trash = set([' ','\n','.','!','?'])

file = open("playground.txt")
data = open("data_analyzed.csv", "w")

writer = csv.writer(data, delimiter = "\t", lineterminator='\n')
    
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

def main(file):
    writer.writerow(["class", "query", "query_parsed", "infinitive", "clicks", "urls"])
    n = file.read().splitlines()[1:]
    for i in range(len(n)):
        parser(n[i])
    data.close()
    return

def parser(json_object):
    enc = 0
    inf = 0
    query = json.loads(json_object)[u'query'].get('qnorm')
    query_parsed = mystem(query)
    if 'инф' in query_parsed:
        inf = 1
    clicks = json.loads(json_object)[u'clicks']
    links = []
    for click in clicks:
        link = click.get("link")
        links.append(link)
    urls = json.loads(json_object)[u'urls']
    for url in urls:
        if ("wikipedia" in url) or ("dic.academic" in url):
            enc = 1
    writer.writerow([enc, query.encode('utf-8'), query_parsed, inf, links, urls])

main(file)

print("it took", time.time() - start, "seconds.")
