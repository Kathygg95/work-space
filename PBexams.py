

# room_rent = int(input())

# statuettes = room_rent - room_rent * 30/100
# catering = statuettes - statuettes*15/100
# sound = catering/ 2 

# total_price = room_rent + statuettes + catering + sound

# print(f'{total_price:.2f}')


# movie = input()
# hall_type = input()
# nb_tickets = int(input())

# if movie == 'A star is Born' and hall_type == 'normal':
#     print(f'{movie} -> {7.5 * nb_tickets} lev.')
# if movie == 'A star is Born' and hall_type == 'luxury':
#     print(f'{movie} -> {10.5 * nb_tickets} lev.')
# if movie == 'A star is Born' and hall_type == 'ultra luxury':
#     print(f'{movie} -> {13.5 * nb_tickets} lev.')
    
# if movie == 'Bohemian Rhapsody' and hall_type == 'normal':
#     print(f'{movie} -> {7.35 * nb_tickets} lev.')
# if movie == 'Bohemian Rhapsody' and hall_type == 'luxury':
#     print(f'{movie} -> {9.45 * nb_tickets} lev.')
# if movie == 'Bohemian Rhapsody' and hall_type == 'ultra luxury':
#     print(f'{movie} -> {12.75 * nb_tickets} lev.')

# if movie == 'Green Book' and hall_type == 'normal':
#     print(f'{movie} -> {8.15 * nb_tickets} lev.')
# if movie == 'Green Book' and hall_type == 'luxury':
#     print(f'{movie} -> {10.25 * nb_tickets} lev.')
# if movie == 'Green Book' and hall_type == 'ultra luxury':
#     print(f'{movie} -> {13.25 * nb_tickets} lev.') 

# if movie == 'The Favourite' and hall_type == 'normal':
#     print(f'{movie} -> {8.75 * nb_tickets} lev.')
# if movie == 'The Favourite' and hall_type == 'luxury':
#     print(f'{movie} -> {11.55 * nb_tickets} lev.') 
# if movie == 'The Favourite' and hall_type == 'ultra luxury':
#     print(f'{movie} -> {13.95 * nb_tickets} lev.') 

# import sys

# nb_movies = int(input())
# contador = 0
# total_rating = 0
# list_rating = []
# list_movie = []

# while contador < nb_movies:
#     movie_name = input()
#     rating = float(input())
#     contador += 1
#     total_rating += rating
#     list_rating = list_rating + [rating]
#     list_movie = list_movie + [movie_name]

# max = list_rating[0]
# min = list_rating[0]
# max_average = list_rating[0]
# max_movie = list_movie[0]
# min_average = list_rating[0]
# min_movie = list_movie[0]
    
# for i in range(0, len(list_rating)): 
#     if list_rating[i] > max:
#         max = list_rating[i]
#         max_average = list_rating[i]
#         max_movie = list_movie[i]
#     if list_rating[i] < min:
#         min = list_rating[i]
#         min_average = list_rating[i]
#         min_movie = list_movie[i] 
        
# print(f'{max_movie} is with highest rating : {max_average}')   
# print(f'{min_movie} is with lowest rating : {min_average}') 
# print(f'Average rating : {total_rating/contador:.1f}') 


# initialize empty dictionary for storing tickets sold
# tickets_sold = {
#     "student": 0,
#     "standard": 0,
#     "kid": 0,
# }
# total_tickets = 0

# # iterate through each screening
# while True:
#     movie_name = input()
#     if movie_name == "Finish":
#         break
        
#     free_seats = int(input())
#     sold_seats = 0
    
#     # iterate through each ticket sold for the current screening
#     while True:
#         ticket_type = input()
#         if ticket_type == "End":
#             break
        
#         tickets_sold[ticket_type] += 1
#         sold_seats += 1
#         total_tickets += 1
        
#     # calculate percentage of hall filled and print results for current screening
#     occupancy_percentage = sold_seats / free_seats * 100
#     print(f"{movie_name} - {occupancy_percentage:.2f}% full.")
    
# # calculate and print total tickets sold and percentage of each ticket type sold
# print(f"Total tickets: {total_tickets}")
# print(f"{tickets_sold['student']/total_tickets*100:.2f}% student tickets.")
# print(f"{tickets_sold['standard']/total_tickets*100:.2f}% standard tickets.")
# print(f"{tickets_sold['kid']/total_tickets*100:.2f}% kid tickets.")

# budget = float(input())
# num_series = int(input())

# total_price = 0

# for i in range(num_series):
#     series_name = input()
#     series_price = float(input())

#     if series_name == "Thrones":
#         series_price *= 0.5
#     elif series_name == "Lucifer":
#         series_price *= 0.6
#     elif series_name == "Protector":
#         series_price *= 0.7
#     elif series_name == "TotalDrama":
#         series_price *= 0.8
#     elif series_name == "Area":
#         series_price *= 0.9

#     total_price += series_price

# if total_price <= budget:
#     left_money = budget - total_price
#     print(f"You bought all the series and left with {left_money:.2f} lv.")
# else:
#     needed_money = total_price - budget
#     print(f"You need {needed_money:.2f} lv. more to buy the series!")


# четене на входните данни
# movie_name = input()
# days = int(input())
# tickets = int(input())
# ticket_price = float(input())
# percent_for_cinema = int(input())

# # изчисляване на общия приход и на печалбата на студиото
# total_income = days * tickets * ticket_price
# cinema_profit = (total_income * percent_for_cinema) / 100
# studio_profit = total_income - cinema_profit

# # отпечатване на резултата
# print(f"The profit from the movie {movie_name} is {studio_profit:.2f} lv.")

# total_tickets = 0
# total_student_tickets = 0
# total_standard_tickets = 0
# total_kid_tickets = 0
# movie_name = input()

# while movie_name != "Finish":
#     free_seats = int(input())
#     movie_tickets = 0

#     while True:
#         ticket_type = input()
#         if ticket_type == "End":
#             break
        
#         movie_tickets += 1
#         total_tickets += 1

#         if ticket_type == "student":
#             total_student_tickets += 1
#         elif ticket_type == "standard":
#             total_standard_tickets += 1
#         elif ticket_type == "kid":
#             total_kid_tickets += 1

#         if movie_tickets == free_seats:
#             break

#     percent_full = movie_tickets / free_seats * 100
#     print(f"{movie_name} - {percent_full:.2f}% full.")

#     movie_name = input()

# percent_student_tickets = total_student_tickets / total_tickets * 100
# percent_standard_tickets = total_standard_tickets / total_tickets * 100
# percent_kid_tickets = total_kid_tickets / total_tickets * 100

# print(f"Total tickets: {total_tickets}")
# print(f"{percent_student_tickets:.2f}% student tickets.")
# print(f"{percent_standard_tickets:.2f}% standard tickets.")
# print(f"{percent_kid_tickets:.2f}% kids tickets.")


# film = input()
# hall_type = input()
# tickets_count = int(input())

# ticket_price = 0

# if film == "A Star Is Born":
#     if hall_type == "normal":
#         ticket_price = 7.50
#     elif hall_type == "luxury":
#         ticket_price = 10.50
#     elif hall_type == "ultra luxury":
#         ticket_price = 13.50
# elif film == "Bohemian Rhapsody":
#     if hall_type == "normal":
#         ticket_price = 7.35
#     elif hall_type == "luxury":
#         ticket_price = 9.45
#     elif hall_type == "ultra luxury":
#         ticket_price = 12.75
# elif film == "Green Book":
#     if hall_type == "normal":
#         ticket_price = 8.15
#     elif hall_type == "luxury":
#         ticket_price = 10.25
#     elif hall_type == "ultra luxury":
#         ticket_price = 13.25
# elif film == "The Favourite":
#     if hall_type == "normal":
#         ticket_price = 8.75
#     elif hall_type == "luxury":
#         ticket_price = 11.55
#     elif hall_type == "ultra luxury":
#         ticket_price = 13.95

# total_income = ticket_price * tickets_count
# print(f"{film} -> {total_income:.2f} lv.")


# airline = input()
# ticket_adults = int(input())
# ticket_child = int(input())
# ticket_adults_price = float(input())
# service_price = float(input())

# ticket_child_price = ticket_adults_price * 0.3

# net_adults = ticket_adults * (ticket_adults_price + 40)
# net_child = ticket_child * (ticket_child_price + 40)
# net_total = (net_adults + net_child)

# profit = net_total / 5

# print(f'The profit of your agency from {airline} tickets is {profit:.2f} lv.')

# import math 
# average_speed = float(input())
# liters_fuel = float(input())

# nb_hours = 384400 * 2/average_speed + 3
# nb_liters = 384400 * 2 / 100 * liters_fuel

# round_hours = math.ceil(nb_hours)
# round_liters = math.ceil(nb_liters)

# print(round_hours)
# print(round_liters)


# width = float(input())
# lenght = float(input())
# height = float(input())
# average_height_astronaut = float(input())

# room_astronaut = 4 * (average_height_astronaut + 0.4)

# volume_ship = width * lenght * height
# capacity = int(volume_ship // room_astronaut)

# if 3<= capacity <= 10:
#     print(f'The spacecraft holds {capacity} astronauts.') 

# elif capacity < 3:
#     print('The spacecraft is too small.')
    
# else:
#     print('The spacecraft is too big.')
    

# month = input()
# hours = int(input())
# nb_people = int(input())
# time_day = input()
# price = 0

# monthList1 = ['march', 'april', 'may']
# monthList2 = ['june', 'july', 'august']


# if (month in monthList1) and time_day == 'day':
#     price = 10.5
    
# if (month in monthList1) and time_day == 'night':
#     price = 8.4
    
# if (month in monthList2) and time_day == 'day':
#     price = 12.6
    
# if (month in monthList2) and time_day == 'night':
#     price = 10.2
    
# if nb_people >= 4:
#         price = price * 0.9
        
# if hours >= 5:
#         price = price*0.5

# costTotal = price * nb_people* hours
        
# print(f'Price per person for one hour: {price:.2f}')
# print(f'Total cost of the visit: {costTotal:.2f} ')
        
# nb_cats = int(input())
# nb_group1 = 0
# nb_group2 = 0
# nb_group3 = 0
# total_grams1 = 0
# total_grams2 = 0
# total_grams3 = 0

# while nb_cats > 0:
#     grams = float(input())
    
#     if 100 <= grams < 200:
#         nb_group1 += 1
#         total_grams1 += grams
          
#     elif 200 <= grams < 300:
#         nb_group2 += 1   
#         total_grams2 += grams
#     else:
#         nb_group3 += 1
#         total_grams3 += grams
    
#     nb_cats -= 1

    
# totatPrice = (total_grams1 + total_grams2 + total_grams3)/ 1000 * 12.45

# print(f'Group 1: {nb_group1} cats.')
# print(f'Group 2: {nb_group2} cats.')
# print(f'Group 3: {nb_group3} cats.')
# print(f'Price for food per day: {totatPrice:.2f} lv.')
        

# contador1 = 0
# contador2 = 0

# while True:
#     enter = input()
    
#     if enter != 'Christmas':
#         age = int(enter)
#         if age <= 16:
#             contador1 += 1
#         else:
#             contador2 += 1    
        
#     else:
#         break
        
        
# money_toys = contador1 * 5
# money_sweater = contador2 * 15

# print(f'Number of adults: {contador2}')
# print(f'Number of kids: {contador1}')
# print(f'Money for toys: {money_toys}')
# print(f'Money for sweaters: {money_sweater}')


# locations = int(input())


# while locations > 0:
#     average_day = float(input())
#     nb_days = int(input())
    
#     total_mined = 0
#     days = 0

#     while nb_days > 0:
#         gold_mined = float(input())
#         total_mined += gold_mined
#         days += 1
#         nb_days -= 1
#     average_real = total_mined / days
    
#     if average_real >= average_day:
#         print(f'Good job! Average gold per day: {average_real:.2f}.')
    
#     else:
#         diff = average_day -  average_real
#         print(f'You need {diff:.2f} gold.') 
        
#     locations -= 1

# print('hello \nworld')
# a = 'hola mundo'
# print(a[2:])
# print(a[::2])
# print(a[::-1])


# with open('text.txt', mode = 'a') as my_new_file:
#     my_new_file.write('\nThank you')
    
# with open('text.txt', mode = 'r') as my_new_file:
#     print(my_new_file.read())

# with open('nuevo.txt', mode = 'w') as f:
#     f.write('Mi nuevo archivo')
    
# with open('nuevo.txt', mode = 'r') as f:
#     print(f.read())
    
# x = open(test.txt, 'w')
# x.write('Hello Wrold')
# x.close()
    
# if 'o' in ['x', 'y', 'z']:
#     print('si')
# else:
#     print('no')
    

# # 1        
# st = 'Print only the words that start with s in this sentence'

# myList = st.split()

# for word in myList:
#     if word[0] == 's':
#         print(word)   

# # 2
# for num in range(11):
#     if num%2 == 0:
#         print(num)

# #3
# st = 'Print every word in this sentence that has an even number of letters'
# myList = st.split()

# for word in myList:
#     if len(word) % 2 == 0:
#         print(word) 

# #4
# for num in range(0,101):
#     if num % 3 == 0 and num % 5==0:
#         print('FizzBuzz')
#     elif num%3 == 0 and num % 5!=0: 
#         print('Fizz')
#     elif num % 5 == 0 and num%3 != 0:
#         print('Buzz') 
#     else:
#         print(num)


#5
st = 'Create a list of the first letters of every word in this string'
thelist = st.split()
mylist = []

for word in thelist:
    mylist.append(word[0])
print(mylist)
           
        



        
        
         
        
        
    
    