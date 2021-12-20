#Lists
"""Multiple items in 1 variable
Can be updated
Built in data type
Used to store collection of datta
created using []
items are in orders with indexed
New items are added at the end of the list with append"""

list = ["a",2,True,"boom"]
print(list)
print(len(list))

#Tuples
""" Multiple items in 1 variable
Build in data type
Presented by ()
Ordered but unchangeable"""

tuple = ("organge","apple",2,2,3.5,True)
print(len(tuple))
print(tuple)

single_tuple=("a",)
print(single_tuple)

#Sets
""" Multiple items in 1 variable
Build in data type
written with {}
unordered, unindexed
duplicate items are not allowed"""

set = {"apple",2,3.5,"cherry",2,3}

print(set)
print(len(set))

#Dictionaries
""" Ordered from python 3.7
Key:value pairs
Created using {}
Build in data type"""


dictionary = {
    "brand" : "Volkswagen",
    "model" : "polo GT",
    "year"  : 2020
    
}

print(dictionary)
print(len(dictionary))
print(dictionary["year"])


#Dictionary does not allow duplicates

