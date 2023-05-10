# try:
#     a = int(input('Ingrese el primer numero: '))
# except:
#     a= 'chanchito feliz'
# if a == 'chanchito feliz':
#     print('Debe insertar solo numeros')
#     exit()
# try:
#     b = int(input('Ingrese el segundo numero:'))
# except: 
#     b= 'chanchito feliz'
# if b == 'chanchito feliz':
#     print('Debe insertar solo numeros')
#     exit()
    
# operacion = input('elija una operacion [+, -, *, /]: ') 


# if operacion== '+':
#     print(a + b) 
# elif operacion== '-':
#     print(a-b)
# elif operacion== '*':
#    print(a*b)
# elif operacion== '/':
#     print(a/b)
# else:
#     print('el simbolo no es valido')

    
    
# #primero = input('Ingrese el num 1: ')

# #try:
# #    primero = int(primero)
# #except:
# #    primero = 'chanchito feliz'
    
# #segundo = input('Ingrese el seg numero: ')
# #try:
# #    segundo= int(segundo)
# #except:
# #    segundo= 'chanchito feliz'
    
# #if primero == 'chanchito feliz' or 'segundo' == 'chanchito feliz':
# #    print('Debe insertar numeros solamente')
# #else:
# #    print(primero + segundo)




# def calculator():
#     a= int(input('Ingrese el valor 1: '))
#     b= int(input('Ingrese el valor 2: '))
    
#     operaciones= input('Ingrese la operacion: +, -, *, /: ')
    
#     if a== ('chanchito') or b== ('chanchito'):
#         print('Debe ingresar numeros')
#     elif operaciones == '+':
#         print(a+b)
#     elif operaciones == '-':
#         print(a-b)
#     elif operaciones == '*':
#         print(a*b)
#     elif operaciones == '/':
#         print(a/b)  
#     else:
#         print('valores incorrectos')
   
# calculator()  


def concatlist(list):
    todo = ''
    for position in list:
        todo = todo + position
    return(todo)
    
concat = concatlist(['pepe', 'lolo'])
print(concat)