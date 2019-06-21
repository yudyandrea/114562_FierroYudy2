# -*- coding: utf-8 -*-
"""

@author: Yudy Andrea Fierro
"""

#EJERCICIO 17

def eliminar_repetidos (lista, longitud):
    ''' Elimina los elementos repetidos de una lista.
        
        Parámetros de entrada:
            lista: Lista a evaluar.
            longitud: Longitud de la lista a evaluar.
        
        Retorna una lista compuesta por cada elemento de la lista original una
        sola vez.
    '''
    
    sin_repetidos= []

    for i in range (longitud):
        if lista[i] not in sin_repetidos:
           sin_repetidos.append(lista[i])

    return sin_repetidos

    
def verificar_mayor(long, lista):    
    ''' Verifica y extrae el número mayor de una lista.
            
        Parámetros de entrada:
            long: Longitud de la lista a evaluar.
            lista: Lista a evaluar.

        Retorna el número mayor encontrado.
    '''
        
    count=-float("inf")       # Count es una variable auxiliar que almacena el
                              # número mayor.
    for i in range (long):   
        if lista[i]>=count:
            count=lista[i]
    
    return count

    
def eliminar_numero(num,lista):
    ''' Remueve un número de una lista. 
        
        Parámetros de entrada:
            num: Número a eliminar.
            lista: Lista de la cual se removerá el número.
        
        NOTA: La función debe ejecutarse al estar seguros de que el número a 
        remover está al menos una vez en la lista. 

        Retorna la lista sin el número indicado.
   '''
       
    lista.remove(num)
    return lista

while True:
    try:
        a = [int(x) for x in input('Ingrese una lista de números enteros:\n').split()]
        if a == []: print ('Ingresó la lista vacía.')    
        else: break
    except ValueError:
        print('La lista debe contener solo números enteros.')

if segundo_mayor != -float("inf"):
    print('\nEl segundo número mayor de la lista ingresada es:', segundo_mayor)

else:
    print('\nLa lista ingresada no tiene un segundo número mayor.')

