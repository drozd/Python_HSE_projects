# -*- coding: utf-8 -*-
vvod=raw_input(unicode('','cp1251').encode('cp866'))
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
import foursquare
import json

#firstly getting all entities' id to the name
client = foursquare.Foursquare(client_id='3XM4S22O2C4HRHW1WSGIVMMNJZPMMYS3YYUFNGS1BNBNJMDY', client_secret='3L3MP0TQBPN05KPMM2AL0DO2L5XNL1AP30TCGDR4GQEKBLXW')
place=client.venues.search(params={'near': 'Moscow', 'limit': 10, 'query': vvod})
tr1=json.dumps(place)
tr2=json.loads(tr1)
tr3=json.dumps(tr2, indent=4, sort_keys=True)
for i in tr2['venues']:
    cafeid=i['id'] #got the entity's id in the dictionary
    #looking for all reviews to every id and writing them to file
    e=client.venues.tips(cafeid)
    pop1=json.dumps(e)
    pop2=json.loads(pop1)
    pop3=json.dumps(pop2, indent=4, sort_keys=True, encoding='utf-8')
    with open ('reviews2.txt', 'a') as outfile:
        for tip in pop2['tips']['items']:
            text=tip['text']
            outfile.write(text+"\n")
    outfile.close()
    #we also can leave only entities with cafe tags
    #no foursquare API modules for python3.Code is in python2.
        
    
