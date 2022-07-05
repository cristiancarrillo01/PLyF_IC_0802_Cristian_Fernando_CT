mi_lista = [1,2,3,4,5,6]
lista_nueva = list(map(lambda x: x * 2, mi_lista))
print(lista_nueva)

print('----------------------------------------------------><----------------------------------------------------')

mi_lista =[18, -3, 5, 0, -1, 12]
lista_nueva = list(filter(lambda x: x > 0, mi_lista))
print(lista_nueva)

print('----------------------------------------------------><----------------------------------------------------')

def multiplicar_por (n):
  return lambda x: x * n

duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)

print(duplicar(4))
print(triplicar(9))
print(diez_veces(11))

print('----------------------------------------------------><----------------------------------------------------')

def cuadrado(x):
    return x ** 2
cuad = lambda x: x ** 2

print(cuadrado(3))
print(cuad(5))

print('----------------------------------------------------><----------------------------------------------------')

enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)
     
print(cuadrados)

print('----------------------------------------------------><----------------------------------------------------')

enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados)

print('----------------------------------------------------><----------------------------------------------------')

enteros = [1, 2, 4, 7]
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3
funciones = [cuadrado, cubo]
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)

print('----------------------------------------------------><----------------------------------------------------')

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x : x % 2 == 0, valores))
print(pares)

print('----------------------------------------------------><----------------------------------------------------')

from functools import reduce
suma = reduce(lambda x, y: x + y, valores)
print(suma)

print('----------------------------------------------------><----------------------------------------------------')


print('----------------------------------------------------><----------------------------------------------------')

