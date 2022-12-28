import collections

cities_by_country = {
    'San Mateo' : 'US',
    'Toronto' : 'CA',
    'Detroit' : 'US',
    'London' : 'UK',
    'Paris' : 'FR',
    'Seattle' : 'US',
    'Vancouver' : 'CA'
}

dct = collections.defaultdict(list)
for city, country in cities_by_country.items():
    dct[country].append(city)

for cities_list in dct.values():
    cities_list.sort()
print(dct)    
    
import pprint
pprint.pprint(dct)