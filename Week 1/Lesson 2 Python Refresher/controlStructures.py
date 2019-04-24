#!/usr/bin/python



# Iteration with loops, there are several options
# 1) for loops : through list or dictionaries
# 2) enumerate: if you need the index values from a list while iterating
# 3) while loops: repeats condition if true

myList = [0,1,2,3,4,5]

#str() casts a datatype to a string
#item is a predefined var that will act as a placeholder, like " i = 0"
for item in myList:
    print ('The value of item is: ' + str(item))
print('*********************')


for i, value in enumerate(myList):
    print('The index value is: ' + str(i) +
          ' The value at i is: ' + str (value))

print('*********************')


i = 0
while(i<10):
    print(1)
    i = i + 1
print('*********************')

#print each key and dictionary value.
# use the in keryword to iterate over dictionary keys

myDict= {
        'a': 'jill',
        'b': 'tom',
        'c': 'tim',
        }

for i in myDict:
    print (i + ', ' + myDict[i])

print('*********************')
