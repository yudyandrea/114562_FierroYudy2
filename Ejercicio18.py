# -*- coding: utf-8 -*-
"""
@author: Yudy Andrea Fierro
"""
#EJERCICIO 18

import copy

def leer_matriz (fila, columna):
    ''' Lee una matriz de un número de filas y columnas específico. 
            
        Retorna la matriz conformada por una lista de listas. 
    '''
        
    matriz= []

    for x in range (fila):  # La matriz se crea utilizando tantas listas vacías
        matriz.append([])   # como filas tenga.

    for i in range (fila): 
        while True:
            try:
                matriz[i]= [int(x) for x in input().split()]
                if matriz[i] == []: print ('No se ingresaron elementos.')
                elif len(matriz[i]) != columna:
                    print ('El número de elementos ingresados debe ser igual '
                           'al número de columnas especificadas.')
                else: break
            except ValueError:
                print('La lista debe contener solo números enteros.')

    return matriz

def matriz_triangular (lista, filas, columnas):
    ''' Convierte una matriz cuadrada en una matriz triangular superior.
       
        Retorna la matriz triangular superior correspondiente (lista de listas)
    '''
    
    for i in range (filas):

        for j in range (columnas):
            if i > j: 
                lista[i][j]=0

    return lista


def posiciones_numero(lista, filas, columnas, numero):
    ''' Busca un número en una lista, y extrae la fila en la que se encuentra.
        
        Retorna una lista con los índices de las filas en las que aparece el nú
        mero solicitado.
    '''
    
    fila_aparicion=[]

    for i in range (filas):

        for j in range (columnas):
            if lista[i][j] == numero:
                fila_aparicion.append(i)

    return fila_aparicion


def mas_apariciones (lista):
    ''' Selecciona en una lista los valores que más se encuentran en ella.
            
        Retorna el o los valores que más se repiten incrementados en 1, y el 
        número de veces que estos aparecen.
    '''
    
    count=0
    fila_max=[]
    count_max =0

    for i in range (len(lista)):       # Iteración en cada fila de la matriz
        count=0

        for j in range(i,len(lista)):  # Contador de apariciones en la lista.
            if lista[j] == i:
                count+=1

        if count == count_max:    # Adición de índices a la lista, que determi
            fila_max.append(i+1)  # nará las filas con mayor incidencia.

        elif count> count_max:
             count_max=count
             fila_max=[i+1]       # Se adiciona 1 por legibilidad al momento de
                                  # la impresión.
    return fila_max, count_max

while True:
    try: 
        fila= int(input('Una matriz cuadrada es aquella que tiene el mismo nú'
                        'mero de filas y de columnas. Ingrese la dimensión de '
                        'la matriz cuadrada: '))
        if fila > 0 : break
    except:
        print ('\nLa dimensión debe ser un entero positivo.')

col= fila     # Por ser matriz cuadrada.

print ('\nIngrese cada fila de la matriz separando sus elementos con un espa'
       'cio, luego, presione enter para continuar con la siguiente fila; los '
       'elementos deben ser números enteros.')
print('\nA=')

A= leer_matriz(fila , col)

U= copy.deepcopy(A)          # Se crea una copia de la matriz original.

triangular=matriz_triangular(U , fila , col)

print ('\nLa matriz triangular asociada a la matriz ingresada es: ')

width = 5

for i in range (len(triangular)):
    print()

    for j in range (len(triangular[1])):
        n=triangular[i][j]  
        print('{0:^{width}}'.format(n, width=width), end=' ')

# Se ejecuta la función y se establecen las condiciones de impresión para la 
# cantidad de unos presentes en la matriz triangular resultante.

filas_con_1= posiciones_numero(triangular, fila, col, 1)

if filas_con_1 == []:
    print('La matriz triangular asociada a la matriz ingresada no contiene nin'
          'gún 1.')

else: #filas_con_20 != []
    fila_con_mas_1, veces= mas_apariciones(filas_con_1)
    
    if len(fila_con_mas_1) == 1: # un solo elemento
        print('\n\nLa fila con más apariciones es:', end=' ')
        print(*fila_con_mas_1, sep=', ', end=' ')
        print('donde el número 1 aparece', veces, 'veces.')
    
    else: # fila_con_mas_20 != []
        fila_con_mas_1, veces= mas_apariciones(filas_con_1)
        print('\n\nLas filas con más apariciones son:', end=' ')
        print(*fila_con_mas_1, sep=', ', end=' ')
        print('donde el número 1 aparece', veces, 'veces.')

