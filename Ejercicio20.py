# -*- coding: utf-8 -*-
"""
@author: Yudy Andrea Fierro
"""
#EJERCICIO 20

import numpy as np

def leer_matriz (fila, columna):
    ''' Lee una matriz de un número de filas y columnas específico.
    
        Retorna la matriz conformada por una lista de listas. 
    '''
  
    matriz= []
    
    for x in range (fila):
        matriz.append([])
    
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

def intercambiar_elementos_fila (matriz):
    ''' Intercambia el orden de los elementos de cada fila de una matriz.
        
        Retorna una nueva matriz con los elementos de cada fila invertidos.
    '''
    
    L2= []
    
    for i in range (0, len(matriz)):
        L2.append([])
        
        for j in range (len(matriz[0])-1, -1, -1):
            L2[i].append (matriz[i][j])
    
    return L2


def rotar_matriz (matriz, L2):
    ''' Rota la matriz indicada 90º en sentido antihorario.
        
        Retorna una lista de listas que representan la matriz girada 90º en sen
        tido antihorario.
    '''
    
    rotada=[]
    
    for i in range (0,len(L2[0])):
        rotada.append([])
        
        for j in range (0,len(L2)):
            rotada[i].append (matriz[j][i])
    
    return rotada
    
while True:
    try: 
        fila= int(input('Ingrese la cantidad de filas que tendrá la matriz: '))
        if fila > 0 : break
    except:
        print ('\nEl número de filas debe ser un entero positivo.')

while True:
    try: 
        col= int(input('Ingrese la cantidad de columnas que tendrá la matriz: '
                       ))
        if col > 0 : break
    except:
        print ('\nEl número de columnas debe ser un entero positivo.')

# Se ejecuta la función leer_matriz para leer las matrices A y B, se imprime un
# encabezado para dar claridad al usuario sobre los datos que está ingresando.

print ('\nIngrese cada fila de la matriz separando sus elementos con un espa'
       'cio, luego, presione enter para continuar con la siguiente fila; los '
       'elementos deben ser números enteros.')

print('\nM=')

# ------------ EJECUCIÓN DE FUNCIONES E IMPRESIÓN DE RESULTADOS ------------- #

matriz= leer_matriz (fila, col)           # Se lee la matriz
L2= intercambiar_elementos_fila (matriz)  # Se invierten los elementos en las 
                                          #filas
rotada= rotar_matriz (matriz, L2)         # Rotar matriz L2
rotada.reverse()                          # Invertir el orden de las filas.

print('\n\nLa matriz rotada 90º en sentido antihorario es: ')

width = 8

for i in range (len(rotada)):
    print()
    
    for j in range (len(rotada[1])):
        n=rotada[i][j]  
        print('{0:^{width}}'.format(n, width=width), end=' ')

# Se convierte la matriz ingresada a un array de Numpy

matriz_np= np.array(matriz)

# Se ejecuta la función que gira la matriz 90º en sentido antihorario

rotada_np= np.rot90(matriz_np)

# Se imprimen los resultados

print('\n\nUtilizando Numpy el resultado obtenido es: ')
print('\n', rotada_np)
