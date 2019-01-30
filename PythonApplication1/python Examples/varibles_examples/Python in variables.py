#!E:/Tools/Python
import sys  # name of the library
import os
import numpy 

#variables Declaration format
var1="'Akshit Meena'";
var2="'Bkshit Meena'";
var3="'Ckshit Meena'";

#List Declaration format
list=['Akshit Meena','Bkshit Meena','Ckshit Meena']
#Dictionary Declaration format
dict_items={
    'Akshit Meena': 101,
    'Bkshit Meena':102,
    'Ckshit Meena':103,
    }
print(var1,var2,var3)   #Printing Variables
print (list)            #printing list
print(list[1], list[2]) #print list in particular values.
print(dict_items)       #Print Dictionary
print(dict_items['Akshit Meena'])#print list in particular values

#changing Value in Dictionary

dict_items['Akshit Meena']=100
print(dict_items)          #Print Dictionary again (update value)

dict_items['Gaurav Meena']=500
print(dict_items)          #Print Dictionary again (new item add value)

# Combination of objects

municipalities = {
    'New York City': ['Manhattan','The Bronx','Brooklyn','Queens','Staten Island'],
    'Tokyo': ['Akihabara','Harajuku', 'Shimokitazawaravi','Nakameguro', 'Shibuya','Ebisu/Daikanyama','Shibuya District','Aoyama','Asakusa/Ueno','Bunkyo District','Ginza','Tsukiji', 'Tsukishima']
}
 
print(municipalities)       #Multupile list toggether

print(municipalities.keys()) #printing Key of dictionary.

print (type(municipalities))                #<class 'dict'> Printing type of functions
print (type(municipalities['Tokyo']))       #<class 'list'> Printing type of functions
print (type(municipalities['Tokyo'][0]))    #<class 'str'> Printing type of functions
    

# Printing the lenght
print (len(municipalities['Tokyo']))        # Printing the no. of word in list.



print(len(municipalities['Tokyo'][2]))       # Printing the no. of String in list.





#--------------

city_population = {
  'Tokyo':100 ,                                  # a key : value pair
  'Los Angeles': 200,
  'New York City': 300,
  'San Francisco': 400,
}

population_values = city_population.values()
print (population_values)                       #printing dictionary value 
print (numpy.mean (population_values))    



