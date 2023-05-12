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
        
    
# def pairnumber (list):
#     pairlist = []
#     oddList = []
    
#     for c in list:
#         if c%2 == 0:
#             pairlist.append(c)
        
#         else:
#             oddList.append(c)
#     print(pairlist)
#     print(oddList)
              
# pairnumber([4, 8, 9, 3, 10])  




# def work_check(work_hours):
    
#     current_max = 0
#     employee_of_month = ''
    
#     for employee, hours in work_hours:
#         if hours > current_max:
#             current_max = hours
#             employee_of_month = employee
            
#     return (employee_of_month, current_max)

# employee, hours = work_check([('Kathy', 200), ('Teo', 400), ('Geri', 150)])
# print(employee)

from random import shuffle
def shuffle_list (mylist):
    shuffle(mylist)
    return mylist
list_shuffled = shuffle_list(['', 'o', ''])

# print(list_shuffled)

def user_guess ():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Select a position: 0, 1, o 2: ')
        return int(guess)
    
theguess = user_guess()

def check_guess(mylist, guess):
    if mylist[guess] == 'o':
        print('Correct')
    else:
        print('Wrong')
        print(mylist)

check_guess(list_shuffled, theguess)

    
        

