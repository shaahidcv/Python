import time

for i in range (10,0,-1):
    print(i)
    time.sleep(.1) #NOTE: delays each print by 1 second

print("hello world")


# NOTE: List [] = mutable, most flexible  , a variable can only contain single value with a list we can contain multiple values.

fruits = ['apple', 'orange','banana','mango']
print(fruits)
print(fruits[0])
fruits.append("pineapple")  #NOTE: add an element to the list.
fruits.remove("orange") #NOTE: remove an element from the list.

# NOTE: fruits.clear() used to remove elements from the list.



for fruit in fruits:
    print(fruit,end=",")


#NOTE: Tuple (): immutable, faster . we cant change the elements in the tuple once its declared. faster to access elements from the tuple.

fruits_tuple = ('apple', 'orange','banana','mango')
print(fruits_tuple)


#NOTE: sets {}: mutable (add/remove) but cant change the elements, unordered so dont support item assignment. no duplicates , best for membership testing.

fruits_set = {'apple', 'orange','banana','mango'}

for fruit in fruits_set:
    print(fruit,end=",")


#NOTE: dictionary : a collection of {key:value} pairs ordered and changeable , no dupicates.

capitals = {"USA":"washington D.C","india":"new delhi","russia":"moscow"}

# print(dir(capitals))

print(capitals.get("USA")) 
capitals.update({"germany":"berlin"})
# popitem() removes latest key value pair 
# 
#captials.keys().
#captials.values().


for key in capitals.keys():
    print(key,end=",")

for key, value in capitals.items():
    print(key,value,end=";")
