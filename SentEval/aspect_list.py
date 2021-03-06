#coding: utf-8

from pymystem3 import Mystem
m = Mystem()
trash = set([' ','\n','.','!','?'])

import codecs
service = {}
food = {}
interior = {}
whole = {}
price = {}

def mystem(sentence):
    sentence = sentence.strip()
    lemmas = m.lemmatize(sentence)
    return lemmas

file = codecs.open('table.csv','r','cp1251')
text = file.readlines()
for line in text:
    line = line.strip().split(',')
    if line[1] == "Service":
	service[line[0]] = line[3]
    elif line[1] == "Food":
	food[line[0]] = line[3]
    elif line[1] == "Interior":
	interior[line[0]] = line[3]
    elif line[1] == "Price":
	price[line[0]] = line[3]
    elif line[1] == "Whole":
	whole[line[0]] = line[3]


#for i in service:
#    u = mystem(i)
#    u = ''.join(u)
#    print u.strip().encode('utf-8')+':','['+service[i]+']'

#for i in food:
#    u = mystem(i)
#    u = ''.join(u)
#    print u.strip().encode('utf-8')+':','['+food[i]+']'

for i in whole:
    u = mystem(i)
    u = ''.join(u)
    print u.strip().encode('utf-8')+':','['+whole[i]+']'

#for i in price:
#    u = mystem(i)
#    u = ''.join(u)
#    print u.strip().encode('utf-8')+':','['+price[i]+']'

#for i in interior:
#    u = mystem(i)
#    u = ''.join(u)
#    print u.strip().encode('utf-8')+':','['+interior[i]+']'



