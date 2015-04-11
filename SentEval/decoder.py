# coding: utf-8
import codecs
file = codecs.open("/home/iluska/dicts_bootstrapped/dicts/food_negative.yml", 'r', 'cp1251')
x = file.read()
print x.encode('utf-8')
