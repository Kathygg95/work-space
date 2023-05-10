# import math

# def FindMiddleValue(list):

#     #list.sort() 4 5 7 9 11
    
#     middle = math.floor(len(list)/2)
#     middleForOdd = middle - 1
    
#     if len(list)%2 == 0:
#         print(list[middle])
#         print(list[middleForOdd])
#     if len(list)%2 != 0:
#         print(list[middle])  
        
# FindMiddleValue(['j', 'g', 't','h', 'u', 't'])



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# kathy = Person("kathy", 27)
# chris = Person("chris", 29)

# kathy2 = { 
#           "name": "kathy",
#            "agexs": 27
#           }

# print(kathy.name)

quesos = ['Cheddar', 'Edam', 'Gouda']
for queso in quesos:
    print(queso)