# -*- coding: utf-8 -*-
"""
@author: Yudy Andrea Fierro
"""

#EJERCICIO 19

def encontrar_subcadena_larga(lista):  
    ''' Busca en una lista la sublista más larga ordenada ascendentemente. 
            
        Retorna la primer sublista más larga encontrada.
    '''

    lista.append(0)  # Se agrega un 0 al final de la lista para que puedan ser
                     # evaluados todos los elementos.
    j= 0   # Almacena temporalmente el índice que determina el fin de la subca-
           # dena más larga encontrada
    a= 0   # Almacena la longitud de la subcadena más larga
    N= []  # Almacena temporalmente los elementos ordenados que va encontrando.
    
    for i in range (1, len(lista)):
        
        if lista[i-1] < lista[i]:   # Elemento anterior menor que el siguiente.
            N.append (lista[i-1])
        
        elif lista[i-1] == lista[i]:# Elemento anterior igual que el siguiente.
            N.append(lista[i-1])
        
        elif len(N) > a:            # Reinicia los valores temporales para el
            a= len(N)               # siguiente iterador
            j= i
            N= []
        
        else: N= []
    
    sublista= lista[(j-1-a) : j]
    
    if sublista== []:  # La sublista ordenada más larga será el primer número 
                       # en caso de no haber otra.
        sublista.append(lista[0])
    
    return sublista

while True:
    try:
        L = [int(x) for x in input('Ingrese una lista de números enteros, sepa'
                                   'rados con un espacio, y finalice con la '
                                   'tecla Enter:\n').split()]
        if L == []: print ('Ingresó la lista vacía.')    
        else: break
    except ValueError:
        print('La lista debe contener solo números enteros.')
          
subcadena_larga= encontrar_subcadena_larga(L)

print ('\nLa primer subcadena ordenada más larga es:', end=' ')
print (*subcadena_larga, sep=', ', end='.')

