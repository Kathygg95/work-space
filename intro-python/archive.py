# man_archivo = open('mbox-short.txt')
# contador = 0
# for linea in man_archivo:
#     contador = contador + 1
# print('Contador de líneas:', contador)

archive = open('text.txt')

for line in archive:
    upperLine = line.upper()
    print(repr(upperLine))