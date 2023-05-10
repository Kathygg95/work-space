# def concatlist(list):

#      todo= ''

#      for posicion in list:
#          todo=todo+posicion
#          print(todo)    
#          return todo          


# concat =concatlist(['pepe','lolo'])
# print(concat)


# def concatlist(list):
#     todo = ''
#     for position in list:
#         todo = todo + position
#         return(todo)
    
# concat = concatlist('pepe', 'lolo')
# print(concat)

# true= 'si'

# if 8>3:
#     print(true)
    
    
# def Dumb(number):
#     return number + 1


# result = Dumb(6)


# def List(list, number):
    
#     for c in list:
#         if c==number:
#             print('el numero esta en la lista')
    
# List([2, 4, 5, 6], 6)
        
    
def pairnumber (list):
    pairlist = []
    oddList = []
    
    for c in list:
        if c%2 == 0:
            pairlist.append(c)
        
        else:
            oddList.append(c)
    print(pairlist)
    print(oddList)
              
pairnumber([4, 8, 9, 3, 10])  


