# if 2 == 2:
#     print('2 es igual a 2')
    
# if 2 == 3:
#     print('2 es igual a 3') 
    
# if 2 > 5:
#     print('2 es mayor a 5')
    
# if 5 > 2:
#     print('5 es mayor a 2')
    
# if 2 != 2:
#     print('2 es distinto a 2')
    
# if 7 != 2:
#     print('7 es distinto a 2')
    
# if 2 >= 3:
#     print('2 es mayor o igual que 3')
    
# if 3 <= 3:
#     print('2 es menor o igual que 3')
    
# if 4 >= 3:
#     print('4 es mayor o igual que 3')
    
# if 1 >= 3:
#     print('1 es mayor o igual que 3')
    
# elif 1 >= 3:
#     print('4 es mayor o igual que 3')
# else:
#     print('ok')
    
# if 1!=1 or 4>2:
#     print('true')

# primero= 'test '
# segundo= 3
# print(primero * segundo)

# prompt = '¿Cual es la velocidad de vuelo de una golondrina sin carga?\n'
# velocidad = input(prompt)


# print(int(velocidad) + 5)

# ent = input('Introduzca la Temperatura Fahrenheit:')

# try:
#     fahr = float(ent)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Por favor, introduzca un número')


    




# try:
#     WorkHours = int(input('Indique cuantas horas: '))
#     PayHour= int(input('Cuanto es la hora:'))
#     if WorkHours> 40:
#         extra = WorkHours - 40
#         salary = 40*PayHour + extra*PayHour*1.5
#         print(salary) 
#     else:
#         print(WorkHours*PayHour)
# except:
#     print('Debe introducir numeros')

# try:
#     puntuacion= float(input('inserte puntuacion: '))
#     if puntuacion >= 0.9 and puntuacion <= 1.0:
#         print('Sobresaliente')
#     if puntuacion >= 0.8 and puntuacion < 0.9:
#         print('Notable')
#     if puntuacion >= 0.7 and puntuacion < 0.8:
#         print('Bien')
#     if puntuacion >= 0.6 and puntuacion < 0.7:
#         print('Suficiente')
#     if puntuacion < 0.6 and puntuacion > 0.0:
#         print('Insuficiente')
# except:
#     print('puntuacion incorrecta')

# import random

# for i in range(10):
#     x = random.random()
#     print(x)

# t = [1, 2, 3]
# a= random.choice(t)
# print(a)




# def repite_estribillo():
#     muestra_estribillo()
#     muestra_estribillo()

# def muestra_estribillo():
#     print('Soy un leñador, que alegría.')
#     print('Duermo toda la noche y trabajo todo el día.')
    
# repite_estribillo()

# def muestra_dos_veces(bruce):
#     print(bruce)
#     print(bruce)
# muestra_dos_veces('Spam '*4)


        
# def Numbers():
    
#     cantidad= 0 
#     total = 0
#     while True:
             
#         try:
#             a = input('Inserte un num: ')
#             num= int(a)
#             print(num)
#             cantidad= cantidad + 1
#             total= total +num
#             media= total/cantidad
            
#         except:
#             if a == 'Fin':
#                 print(cantidad, total, media)
#                 break
#             else:
#                 print('Error')
            
# Numbers()

# fruta = 'banana'
# for caracter in fruta:
#     print(caracter)
# indice = -1

# while indice > -len(fruta):
#     print(fruta[indice])
#     indice = indice -1

# fruta = 'banana'
# print(fruta[:])

# fruta = 'banana'
# contador = 0

# for caracter in fruta:
#     if caracter == 'a':
#         contador = contador + 1
# print(contador)    

# def Counting_words (word, a):
    
#     counting = 0
    
#     for c in word:
#         if c== a:
#             counting= counting+1
#     print(counting)
    
# Counting_words('ferrocarril', 'r')

# word = 'geeks for geeks'
# print(word.find('for'))
# print(word.count('e'))

# str = 'X-DSPAM-Confidence:0.8475'
# part = str.find(':') + 1
# print(str[part:])

# flo= float(str[part:])
# print(flo)

# print(str.isdigit())

# cosa = 'hola\nmundo'
# print(cosa)

