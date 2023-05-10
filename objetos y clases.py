# class Usuario:
#     nombre = 'Felipe'
#     apellido= 'Feliz'

# usuario = Usuario()

# print(usuario.nombre, usuario.apellido)


# class Usuario:
#     def __init__ (self, nombre, apellido, edad, email):
#          self.nombre= nombre
#          self.apellido= apellido
#          self.edad= edad
#          self.email= email
    
#     def NombreCompleto(self):
#         return self.nombre+' ' + self.apellido +' '+ str(self.edad) +' '+ self.email
        
# usuario= Usuario('Felipe', 'Feliz', 43, 'felipe@gmail.com')
# usuario2= Usuario('Chanchito', 'Feliz', 36, 'chan@gmail.com')

# nombreCompleto = usuario.NombreCompleto()
# nombreCompleto2 = usuario2.NombreCompleto()
# print(nombreCompleto)
# print(nombreCompleto2)

#print(usuario.nombre, usuario.apellido, usuario.edad, usuario.email, usuario2.nombre, usuario2.apellido, usuario2.edad, usuario2.email)



# class Usuario:
#     def __init__ (self, nombre, apellido):
#         self.nombre= nombre
#         self.apellido= apellido
           
#     def saludo(self):
#         print('hola!, mi nombre es, self.nombre, self.apellido')
        
# usuario= Usuario('Felipe', 'Feliz')
# usuario2= Usuario('Chanchito', 'Feliz')

# usuario.saludo()
# usuario2.saludo()

# class BankAccount:
#     def __init__(self, name, lastname, amount):
#         self.name = name 
#         self.lastname = lastname
#         self.amount = int(amount)
        
#     def WithdrawMoney(self, a):
#         if a <= self.amount:
#             self.amount = self.amount - a
#             return a
#         else:
#             print('No hay disponibilad')
            
#     def AmountRemaining(self):
#         return self.amount
    
# usuario = BankAccount('Kathy', 'Garcia', 100)   


# usuario.WithdrawMoney(60)
# print(usuario.AmountRemaining())
# usuario.WithdrawMoney(40)       
# print(usuario.AmountRemaining())
# usuario.WithdrawMoney(40)       


# class BankAccount:
#     def __init__ (self, name, lastname, amount):
#         self.name = name
#         self.lastname = lastname
#         self.amount = amount
    
#     def WithdrawMoney (self, a):
#         if a <= self.amount:
#             self.amount= self.amount - a
#             return a
#         else:
#             print('no hay disponibilidad')
    
#     def Remaining(self):
#         return self.amount
    


# class PhoneDirectory:
#     def __init__(self, name, number):
#         self.directory = {}
#         self.directory[name] = number
        
        
#     def IdentifyNumber(self, name):
#         return self.directory[name]
    
#     def Savedetails(self, name, number):
#         self.directory[name] = number
        
# Client1= PhoneDirectory('Felipe', 105342)

# print(Client1.IdentifyNumber('Felipe'))
# print('00'+ str(Client1.IdentifyNumber('Felipe')))



# class List:
#     def __init__(self, list):
#         self.list = list
        
#     def Plus(self, number):
#         for c in range(0,len(self.list)):
#             self.list[c] = self.list[c] * number
#         return self.list
            
