#/usr/bin/python

# Maps have key value pair


#### Sets
# comparable to list and also vaguely a collection of things, but with one big difference

# A List as an ordering system to it, sets do not have this but do not allow duplicate elements
# a set us comparable to a bag, you can reach for its elements but you never know what order its coming out in

### A map is a set-based data structure, similar to an array being a list based datastructure.
# Map = <key,value> a group of keys is a set. the keys in a map are a set.
# The keys of a map, like the words in a dictionary need to be unique
# a WORD can have multiple definition, in this case the WORD is a key and its definitions are its values.
# A map can be like a dictionary, it will not have the same word more than once.
# a group of unique keys without any order is called a set.

# In python Maps appear as dictionaries.

udacity = {}
udacity['u'] = 1
udacity['d'] = 2
udacity['a'] = 3
udacity['c'] = 4
udacity['i'] = 5
udacity['t'] = 6
udacity['y'] = 7

print (udacity)
# {'u': 1, 'd': 2, 'a': 3, 'c': 4, 'i': 5, 't': 6, 'y': 7}
print (udacity['t'])

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

usa_sorted = sorted(locations['North America']['USA'])
print (1)
for city in usa_sorted:
    print (city)

asia_cities = []
print (2)
for countries, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countries
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)
