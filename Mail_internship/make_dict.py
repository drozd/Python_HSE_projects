#!/usr/bin/python
# Transforming JSON into CSV for machine learning
# coding: utf-8

import codecs, json, re

file = codecs.open('playground.txt', 'r', 'utf-8')
data = file.readlines()
file.close()

dic = {}
id_num = 0

outfile = codecs.open('Clean_data.tsv', 'w', 'utf-8')
outfile.write('text' + '\t' + 'browser' + '\t' +
                  'time' + '\t' + 'utype' + '\t' +
                  'is_navig' + '\t' + 'porno_type' + '\t' +
                  'searcher' + '\t' + 'age' + '\t' +
                  'clicks' + '\t' + 'urls' + '\t' +
                  'encyc' + '\n')

for line in data:
    id_num += 1
    text = re.findall(u'"qnorm": (.*?),', line)
    browser = re.findall(u'user_agent": (.*?),', line)
    time = re.findall(u'time": (.*?),', line)
    utype = re.findall(u'"utype": (.*?),', line)
    is_navig = re.findall(u'"is_navig": (.*?),', line)
    porno_type = re.findall(u'"porno_type": (.*?),', line)
    searcher = re.findall(u'"searcher": (.*?),', line)
    age = re.findall(u'"age": (.*?),', line)
    clicks = re.findall(u'"link": (.*?),', line)
    clicks_pos = re.findall(u'"pos": (.*?),', line)
    urls = re.findall(u'"urls": (.*?)}', line)
    encyc = 0
    
    if len(clicks) != 0:
        
        result = str(clicks[0])
        query = str(text[0])
        if 'wiki' in result:
            encyc = 1 # that means encyclopedic query
        elif 'dip.academ' in result:
            encyc = 1 # that means encyclopedic query
        elif 'wiki' in query:
            encyc = 1 # that means encyclopedic query
        else:
            encyc = 0 # NOT encyclopedic

    dic[id_num] = {"text" : text[0], "browser" : browser,
                   "time" : time[0], 'utype' : utype[0],
                  'is_navig' : is_navig, 'porno_type' : porno_type,
                   'searcher' : searcher, 'age' : age,
                   'clicks' : clicks, 'urls' : urls,
                   'encyclopedic' : encyc}
    
    outfile.write(str(text[0]) + '\t' + str(browser).strip('[]') + '\t' +
                  str(time[0]).strip('[]') + '\t' + str(utype).strip('[]') + '\t' +
                  str(is_navig).strip('[]') + '\t' + str(porno_type).strip('[]') + '\t' +
                  str(searcher).strip('[]') + '\t' + str(age).strip('[]') + '\t' +
                  str(clicks).strip('[]') + '\t' + str(urls).strip('[]') + '\t' +
                  str(encyc) + '\n')    
    
outfile.close()
