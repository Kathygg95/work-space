

# n = int(input())
# current = 1
# current_bigger_than_n = False

# for row in range(1, n + 1):
#     for column in range(1, row + 1):
        
#         if current > n:
#             current_bigger_than_n = True
#             break
        
#         print(str(current) + " " , end=" ")
#         current += 1
        
#     if current_bigger_than_n:
#         break
#     print()                
        
    

# first_number = int(input())
# second_number = int(input())

# for number in range(first_number, second_number + 1):
#     number_to_str = str(number)
#     even_sum = 0
#     odd_sum = 0 
    
#     for index, digit in enumerate (number_to_str):
#         if index % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
    
#     if even_sum == odd_sum:
#         print(number, end= " ")
                


# is_prime = True
# prime_sum = 0
# non_prime_sum = 0

# input_line = input()

# while input_line != "stop":
#     current_num = int(input_line)
#     if current_num < 0:
#         print("Number is negative.")
#     else:
#         for i in range(2, current_num):
#             if current_num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             prime_sum += current_num
#         else:
#             non_prime_sum += current_num
#             is_prime = True
 
#     input_line = input()
 
# print(f"Sum of all prime numbers is: {prime_sum}")
# print(f"Sum of all non prime numbers is: {non_prime_sum}")
  
        
# prime_sum = 0
# non_prime_sum = 0
# is_prime = True

# n = input()

# while n != 'Stop':
#     number = int(n)
     
#     if number < 0:
#         print('Number is negative')
    
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if number % i != 0:
#             prime_sum += number  
#             is_prime = True 
#         else:
#             non_prime_sum += number
    
#     n = input()        
        
# print(f'Sum of all prime numbers is: {prime_sum}')
# print(f'Sum of all non prime numbers is: {non_prime_sum}')



        
    
   
        
    
    
