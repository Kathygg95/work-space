# from modulos import saludo, mascotas

# print(mascotas)
# saludo('Nicolas')

from camelcase import CamelCase

c = CamelCase()
s = 'esta oracion necesita CamelCase'

camelcased = c.hump(s)

print(camelcased) 