
# number = int(input())
# k = 1

# while k <= number:
#     print(k)
#     k= k*2 + 1
    
    
# inpt = input()
# balance = 0.0

# while inpt != 'NoMoreMoney':
#     amount = float(inpt)
#     if amount < 0:
#         print('output')
#         break
#     balance += amount 
#     print(f'Increase: {amount:.2f}')
#     inpt = input()
# print(f'Total: {balance:.2f}')

# inpt = input()
# max = -10000000000000

# while inpt != 'Stop':
#     num = int(inpt)
#     if num > max:
#         max = num
#     inpt = input()
# print(max)
        
# book_name = input()
# book_count = 0
# is_book_found = False

# current_book = input()
# while current_book != 'No more books':
#     if current_book == book_name:
#         is_book_found = True
#         print(f'You checked {book_count} books and found it')
#         break
    
#     book_count += 1
#     current_book = input()
    
# if not is_book_found:
#     print('The book you search is not here')
#     print(f'You checked {book_count} books')

# failed_threshold = int(input())
# failed_times = 0
# solved_problems_count = 0
# grades_sum = 0
# last_problem = ''
# has_failed = True   

# while failed_times < failed_threshold:
#     problem_name = input()
#     if problem_name == 'Enough':
#         has_failed = False
#         break
#     grade = int(input())
#     if grade <= 4:
#         failed_times += 1
#     grades_sum += grade
#     solved_problems_count += 1
#     last_problem = problem_name
    
# if has_failed:
#     print(f'You need a break, {failed_threshold} poor grades')
# else:
#     print(f'Average score: {grades_sum/solved_problems_count:.2f}')
#     print(f'Number of problems: {solved_problems_count}')
#     print(f'Last problem: {last_problem}')
        
    
    
# excursion= float(input())
# on_hand = float(input()) 

# action = ''
# amount = 0
# days_counter = 0
# spending_counter = 0

# while on_hand < excursion:
#     action = input()
#     amount = float(input())
#     days_counter += 1
    
#     if action == 'save':
#         on_hand = on_hand + amount
#         spending_counter = 0    
      
#     elif action == 'spend':
#         on_hand -= amount
#         spending_counter += 1 
#         if on_hand < 0:
#             on_hand = 0
        
# if spending_counter == 5:
#     print('You cant save money')
#     print(f'{days_counter}')
    
# else:
#     print(f'You saved the money for {days_counter} days')



    
            
# nb_of_steps = 0
# total_nb_of_steps = 0
# nb_of_steps_returning_home = 0
# total_nb_of_steps_after_returning_home = 0
 
# while total_nb_of_steps < 10000:
#     command = input()
 
#     if command == "Going home":
#         nb_of_steps_returning_home = int(input())
#         total_nb_of_steps += nb_of_steps_returning_home
#         break
 
#     nb_of_steps = int(command)
#     total_nb_of_steps += nb_of_steps
 
# if total_nb_of_steps >= 10000:
#     diff = total_nb_of_steps - 10000
#     print(f"Goal reached! Good job!")
#     print(f"{diff} steps over the goal!")
# else:
#     diff = 10000 - total_nb_of_steps
#     print(f"{diff} more steps to reach goal.")    
    
            
# steps = 0    
# total_steps = 0
# steps_home = 0

# while total_steps < 10000:
#     command = input()
    
#     if command == 'Going home':
#         steps_home = int(input())
#         total_steps = total_steps + steps_home
#         break 
    
#     steps = int(command)
#     total_steps += steps
    
# if total_steps >= 10000:
#     diff = total_steps - 10000
#     print('Goal reached ! Good job !')
#     print(f'Goal reached! Good job! {diff} steps over the goal')
    
# else:
#     diff = 10000 - total_steps
#     print(f'{diff} more steps to reach goal ')        


# enter = float(input())
# money = round(enter * 100)
# nb_coins = 0

# while money > 0:
    
#     if money >= 200:
#         money -= 200
#         nb_coins += 1
        
#     elif 200 > money >= 100:
#         money -= 100
#         nb_coins += 1
        
#     elif 100 > money >= 50:
#         money -= 50 
#         nb_coins += 1
    
#     elif 50 > money >= 20:
#         money -= 20 
#         nb_coins += 1 
        
#     elif 20 > money >= 10:
#         money -= 10 
#         nb_coins += 1
        
#     elif 10 > money >= 5:
#         money -= 5 
#         nb_coins += 1
        
#     elif 5 > money >= 2:
#         money -= 2 
#         nb_coins += 1
    
#     elif 2 > money >= 1:
#         money -= 1 
#         nb_coins += 1
        
# print(nb_coins)
        
    
# length = int(input())
# width = int(input())
# nb_pieces = length * width
# pieces_taken = 0

# while nb_pieces >= 1:
#     piece = input()
    
#     if piece == 'STOP':
#         diff = nb_pieces - pieces_taken
#         print(f'{diff} pieces are left')    
#         break
#     intPiece = int(piece)
        
#     if intPiece <= nb_pieces: 
#         pieces_taken += intPiece
#         rest = nb_pieces - pieces_taken
        
#     if intPiece > rest:
#         diff = intPiece - rest
#         print(f'No more cake left! You need {diff} pieces more')


length = int(input())
width = int(input())
height = int(input())

nb_boxes = length * width * height 
boxes_in = 0

while nb_boxes >= 1:
    box = input()
    
    if box == 'Done':
        diff = nb_boxes - boxes_in
        print(f'{diff} Cubic meters left')    
        break
    
    intbox = int(box)
        
    if intbox <= nb_boxes: 
        boxes_in += intbox
        rest = nb_boxes - boxes_in
        
    if 0 > rest:
        diff = 0 - rest
        print(f'No more free space! You need {diff} Cubic meters more')        
