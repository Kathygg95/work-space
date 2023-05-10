      #conditionals

# import math
# time_first = int(input())
# time_second = int(input())
# time_third = int(input())

# total_time= time_first + time_second + time_third

# minutes = total_time / 60
# seconds = total_time % 60

# minutes = math.floor(minutes)

# if seconds < 10:
#     print(f'{minutes}:0{seconds}')
# else:
#     print(f'{minutes}:{seconds}')


# num = input()
# number= int(num)
# bonus =0
# if number <= 100:
#     bonus = 5
# elif number > 100 and number<=1000:
#     bonus = number/5
# else:
#     bonus= number/10
    
# if number%2 == 0:
#     bonus+= 1
# elif number % 10 ==5:
#     bonus+= 2
   
# total = number + bonus
# print(bonus)
# print(total)


# hour = int(input())
# minutes = int(input())
# minutes_plus = minutes + 15

# if hour < 23 and minutes_plus >= 60:
#     hour = hour + 1
#     min = 15 -(60 - minutes)
#     print(f'{hour}:0{min}') 
# elif hour == 23 and minutes >= 45:
#     min = 15 -(60 - minutes)
#     if min < 10:
#         print(f'{00}:0{min}')  
#     else:
#         print(f'{00}:{min}')    
    
# else : 
#     print(f'{hour}:{minutes_plus}') 

# excursion = float(input('Price of Excursion: '))
# puzzle = int(input('Amount of puzzles: '))
# doll = int(input('Amount of dolls: '))
# bear = int(input('Amount of bears: '))
# mignon = int(input('Amount of mignons: '))
# truck = int(input('Amount of trucks: '))

# #Products * prices 
# puzzle_in = 2.60 * puzzle
# doll_in = 3 * doll
# bear_in = 4.10 * bear 
# mignon_in = 8.20 * mignon
# truck_in = 2 * truck

# total = puzzle + doll + bear + mignon + truck
# total_in = puzzle_in + doll_in + bear_in + mignon_in + truck_in
# discount = total_in/4

# if total >= 50:
#     rent = (total_in - discount)/10
#     remaining = total_in - (rent + discount)
    
#     if remaining >= excursion:
#         money = remaining - excursion
#         print(f'Yes, {money} lv left')
#     else:
#         need = excursion - remaining 
#         print(f'Not enough money, {need} lv needed')  
# else:
#     rent = total_in/10
#     money = total_in - rent
#     if money >= excursion:
#         print(f'Yes, {money} lv left')
#     else:
#         need = excursion - money 
#         print(f'Not enough money, {need} lv needed')
    
        
        
# movie_budget = float(input())
# number_of_extras = int(input())
# cost_of_clothing = float(input())

# total_clothing = number_of_extras * cost_of_clothing        
# set = movie_budget*0.1     

# if number_of_extras > 150:
#     total_clothing = total_clothing - total_clothing*0.1
# else: 
#     total_clothing = total_clothing
 
# total_cost = set + total_clothing   
# missing = total_cost - movie_budget
# remaining= movie_budget - total_cost

# if total_cost > movie_budget:
#     print(f'Not enough money!, Wingard _ needs {missing:.2f} left more .')

# else:
#     print(f'Action!, Wingard starts filming with {remaining:.2f} leva left.')
    

# flower = input('')
# number = int(input())
# budget = int(input())

# if flower == 'Rose':
#     if number > 80:
#         cost = number*5*0.9
#     else: 
#         cost= number*5
        
# if flower == 'Dahlia':
#     if number > 90:
#         cost = number*3.8*0.85
#     else: 
#         cost = number*3.8
        
# if flower == 'Tulip':
#     if number > 80:
#         cost = number*2.8*0.85
#     else: 
#         cost = number*2.8

# if flower == 'Narcissus':
#     if number < 120:
#         cost = number*3*1.15
#     else: 
#         cost = number*3        

# if flower == 'Gladiolus':
#     if number < 80:
#         cost = number*2.5*1.2
#     else: 
#         cost = number*2.5  

# if cost <= budget:
#     remaining= budget-cost
#     print(f'Hey , you have a great garden with {number} {flower} and {remaining:.2f} leva left .')

# else: 
#     missing= cost-budget
#     print(f'Not enough money , you need {missing:.2f} leva more')



# for i in range(1, 101):
#     print(i)
 
 
# word = input('')
# sum = 0

# for c in word:
#     if c == 'a':
#         sum = sum + 1
#     elif c== 'e':
#         sum = sum + 2
#     elif c == 'i':
#         sum = sum + 3
#     elif c== 'o':
#         sum = sum+ 4
#     elif c== 'u':
#         sum = sum + 5
# print(sum)
    
    
# quantity = int(input())
# sum = 0
# for i in range(quantity):
#     num = int(input())
#     sum = sum + num
# print(sum)
    
    
# import sys
# smallest= sys.maxsize
# biggest = -sys.maxsize

# quantity = int(input())

# for i in range(quantity):
#     num= int(input()) 
#     if num > biggest:
#         biggest = num
#     if num < smallest:
#         smallest = num 
# print(f'Max num is {biggest}, and Min num is {smallest}')
    
# x = int(input())
# sum_left= 0
# sum_right=0

# for i in range(0, x):
#     num = int(input())
#     sum_left = sum_left+ num
    
# for j in range(0, x):
#     num = int(input())
#     sum_right= sum_right+ num
    
# if sum_left == sum_right:
#     print(f'yes, sum = {sum_right}')
# else:
#     diff= abs(sum_right-sum_left)
#     print(f'no, diff is {diff}')
    
# n= int(input('cuantos num: '))
# sum_odd= 0
# sum_even= 0

# for i in range(1, n+1):
#     num= int(input()) 
#     if i%2 ==0:
#         sum_even= sum_even + num     
#     else:
#         sum_odd= sum_odd + num
   
# if sum_odd == sum_even:
#     print('yes')
#     print(f'Sum= {sum_even}')
# else:
#     diff = abs(sum_even-sum_odd)
#     print('no') 
#     print(f'Diff = {diff}')


# time = int(input())
# minutes = int(input())
# arrivalT = int(input())
# arrivalMin = int(input())

# exam = time*60 + minutes
# arrival = arrivalT*60 + arrivalMin
# retard = arrival- exam
# advance = exam - arrival

# if exam == arrival:
#       print('On time')
# elif 0<advance <= 30:
#       print(f'On time, {advance} minutes before the start')
      
# elif arrival> exam:
#       if retard < 60:  
#             print(f'Late, {retard} minutes after the start')
#       else:
#             print('Late')
            
#             if retard%60 < 10:
#                   print(f'{int(retard/60)}:0{int(retard%60)} hours after the start') 
#             else: 
#                   print(f'{int(retard/60)}:{int(retard%60)} hours after the start')
      
# elif advance > 30:
#       if advance< 60:
#             print(f'Early, {advance} minutes before the start')
#       else:
#            print('Early')
            
#            if exam%60 < 10:
#                print(f'{int(advance/60)}:0{int(advance%60)} hours before the start') 
#            else: 
#                print(f'{int(advance/60)}:{int(advance%60)} hours before the start')       


# for num in range(7, 1001):
#       if num % 10 == 7:
#             print(num)
            
# for num in range(7, 1001, 10):
#       print(num)

# import sys

# enter = int(input())
# sum = 0
# mxm = -sys.maxsize

# for i in range(0, enter):
#     num = int(input())
#     sum += num
      
#     if num > mxm:
#         mxm = num
            
# if mxm == sum - mxm:
#     print(f'yes, sum = {mxm}') 
# else: 
#     diff = abs(mxm - (sum-mxm))
#     print(f'No, Diff = {diff}') 

# age = int(input())
# price_machine = int(input())
# toy_price = int(input())
# total_toy_price = 0
# even_money = 0
# increase = 0

# for i in range(1, age+1):
#     if i%2 != 0:
#         total_toy_price += toy_price
#     else:
#         increase = increase+ 10
#         even_money = even_money + increase
        
# bro_money = age/2 
# total_money = total_toy_price + even_money - bro_money

# if total_money >= price_machine:
#     diff1 = total_money - price_machine       
#     print(f'Yes! {diff1}')
# else:
#     diff2 = price_machine - total_money
#     print(f'No, {diff2}')


  
# n_of_open_browsers = int(input()) 
# salary = int(input())

# for i in range (0, n_of_open_browsers):
#     website_name = input()
#     if website_name == 'Facebook':
#         salary -= 150
#         if salary <= 0:
#             print('You have lost your salary')
#             break
        
#     elif website_name == 'Instagram':
#         salary -= 100
#         if salary <= 0:
#             print('You have lost your salary')
#             break
    
#     elif website_name == 'Reddit':
#         salary-=50
#         if salary <= 0:
#             print('You have lost your salary')
            
#     else:
#         salary -= 0
        
# if salary > 0:
#     print(f'{salary}')            
          
          
# groups = int(input())
# musala = 0 
# montBlanc = 0
# kilimanjaro = 0
# k2 = 0
# everest = 0

# for i in range(0, groups):
#     people = int(input())
#     if people <= 5:
#         musala = musala + people
        
#     elif 6<= people<= 12:
#         montBlanc = montBlanc + people
        
#     elif 13< people < 25:
#         kilimanjaro = kilimanjaro + people
        
#     elif 26< people < 40:
#         k2 = k2 + people
        
#     elif people > 41:
#         everest = everest + people
 
# total = musala + montBlanc + kilimanjaro + k2 + everest       
# print(100*musala/total)
# print(100*montBlanc/total)
# print(100*kilimanjaro/total)
# print(100*k2/total)
# print(100*everest/total) 
           
         


