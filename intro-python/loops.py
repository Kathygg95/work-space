# # i=1

# # while i<8:
# #     print(i)
# #     i+=1
# #     if i== 5:
# #         break

# # i=1

# # while i<8:
# #     i+=1
# #     if i== 5:
# #         continue
# #     print(i)

# # numeros = [1, 2, 3, 4, 5]
# # suma = 0
# # for numero in numeros:
# #     suma = suma + numero
# # print(suma)

# usuarios = ['felipe', 'marcos', 'alfonso', 'amador']

# # for usuario in usuarios:
# #     print(usuario)

# # for usuario in usuarios:
# #     if usuario == 'marcos':
# #         break
# #     print(usuario)

# # for usuario in usuarios:
# #     if usuario == 'marcos':
# #         continue
# #     print(usuario)

# # for rango in range (4, 40, 4):
# #     print(rango)
# # else:
# #     print('hemos terminado')

# # usuarios = ['felipe', 'marcos', 'alfonso', 'amador']
# # edades = [4, 5, 67, 58]

# # for usuario in usuarios:
# #     for edad in edades:
# #         print(usuario, edad)

# # numeros = [3, 5, 2, 76, 32, 1]
# # tamanoLista = range(1, len(numeros)) #[1,2,3,4,5,6]
# # max = numeros[0]

# # for posicion in tamanoLista:
# #     if max < numeros[posicion]:
# #         max = numeros[posicion]

# # print(max)


# #numeros = [3, 5, 2, 76, 32, 1]

# def mayornumero(numeros):
#     max = numeros[0]

#     for numero in numeros:
#         if max < numero:
#             max = numero
#     print(max)

# mayornumero([5, 64, 88, 69, 53])

# # numero = int(input('Ingrese un numero: '))
# # descomposicion = range(numero)
# # total = 1

# # for factorial in descomposicion:
# #         total = factorial * total
# # print(total)

# #lista = ['hola', 'dedo', 'feo', 'gente', 'jaula']


# def concatlist(list):

#     todo= ''
#     posicion= list[0]

#     for posicion in list:
#         todo=todo+posicion
#     print(todo)


# concatlist(['pepe','lolo'])

# def oddnumbers ():

#     a= int(input('Ingrese el numero: '))
#     list= range(1,a)

#     for odd in list:
#         if odd %2 != 0:
#             print(odd)
#         odd=odd+1

# oddnumbers ()

# def word(input):
#     for w in input:
#         print(w)

# word('chanchito')

# def Equalwords ():

#     str1= input('ingrese palabra 1: ')
#     str2= input('ingrese palabra 2: ')

#     if len(str1) != len(str2):
#         print("No son iguales")
#         return

#     for c in range(len(str1)):
#         if str1[c] != str2[c]:
#             print("No son iguales")
#             return
#     print(" Son iguales")

# Equalwords()

# def Highestnumber (list):

#     max = list[0]

#     for number in list:
#         if number > max:
#              max =  number
#     print(max)

# Highestnumber ([3, 5, 7, 24, 1])

# def Average (list):

#     suma= 0

#     for number in list:
#         suma= suma + number
#     average = int(suma) / len(list)
#     print(average)

# Average ([67, 5, 7, 24, 1])


# def PrimeNumber (x):

#     b= 2

#     while b!= x:
#         if x % b == 0:

#             print('no es primo')
#             return
#         else:
#             b= b+ 1
#     print('es primo')


# PrimeNumber (7)


# def PrimeNumberWithFor(x):

#     for b in range(2, x-1):
#         if x%b == 0:
#             print("no es primo")
#             return

#     print(" es primo")

# PrimeNumberWithFor(8)


# def pairnumber (list):
#     pairlist = []
#     for c in list:
#         if c%2 == 0:
#             pairlist.append(c)
#     return pairlist

# print(pairnumber([4, 8, 9, 3, 10]))


# def MinNumber (list):

#     min = list[0]

#     for number in list:
#         if number < min:
#             min= number
#     print(min)

# MinNumber([4, 3, 2, 1, 9, 6])


# def ConcatLists(list1, list2):

#     combinatedList = []

#     for number in list2:
#         list1.append(number)
#         combinatedList= list1
#     print(combinatedList)

# ConcatLists([2, 4, 5], [3, 6, 7])

# def oddnumbers (a):

#     list= range(1,a)
#     oddlist = []

#     for odd in list:
#         if odd %2 != 0:
#             oddlist.append(odd)
            
#     return oddlist



# odds = oddnumbers(20)
# print(odds)


# def WordPrefix (word, suffix):

#     listLong = range(len(suffix))
   
#     suffixLong= range(len(word))
   
#     for c in listLong:
#         for l in suffixLong:       
#             if suffix[c] != word[c]:  
#              print('no son iguales')
#             return
    
#     print('son iguales')   
                     
# WordPrefix ('gitano', 'ano')
 
               
# def WordPrefix (word, suffix):

#     index1 = len(word)-1
#     index2 = len(suffix)-1
   
#     while index1 >= 0 and index2 >= 0:
#         if suffix[index2] != word[index1]: 
#             print('no son iguales')
#             return
#         index1 = index1 - 1
#         index2 = index2 - 1
    
#     print('son iguales')   

# WordPrefix('gitaano', 'aano')

# def Palindrome (word):
    
#     back = len(word) - 1
#     front = 0
    
#     while back >= 0:
#         if word[front] != word[back]:
#             print('no es palidrome')
#             return
#         back = back - 1
#         front= front + 1
        
#     print('si es')
    
# Palindrome ('arepera')   




# def Minimum (a, b):
    
#     if a > b:
#        return b
#     return a
     
# def Addition (str1, str2):
    
#     position = 1
#     save= ''
#     reminder= 0
    
#     while position <= Minimum(len(str1), len(str2)):
#         sum = int(str1[-position]) + int(str2[-position]) + reminder
#         if sum > 9:
#             reminder = 1
#             sum -= 10
#         position += 1
#         save =  str(sum) + save
#     return save
    
# print(Addition ('8888845', '8769'))



# def TextList (text):

#     list= []
#     str= ""    
#     length = len(text) - 1
    
#     for c in text:
#         if c != ' ':
#             str = str + c 
#         elif c == ' ' or c == text[length]:
#             list.append(str)
#             str = "" 
        
#     return list         

# print(TextList('Las hojas se mueven'))


#position= [range(len(text))] 

x = 2* (3-1)
print(x)