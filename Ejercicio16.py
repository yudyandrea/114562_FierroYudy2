# -*- coding: utf-8 -*-
"""

@author: Yudy Andrea Fierro
"""

#EJERCICIO 16

def verificar_orden(long, lista):
    ''' Verifica si una lista está ordenada comparando dos elementos sucesivos.
        
        Parámetros de entrada:
            long: Longitud de la lista a evaluar.
            lista: Lista de números a evaluar.

        Retorna el contenido de una variable auxiliar, que, en caso de que la  
        lista esté ordenada, su valor debe ser igual a cero.
    '''
        
    count=0

    for i in range (long-1):
        if lista[i] > lista[i+1]:
            count += 1
            break

    return count


def anadir_numero(num, lista): 
    ''' Añade un número a una lista ordenada en la posición correspondiente.
        
        Parámetros de entrada:
            num: Número a añadir a la lista.
            lista: Lista a la que será añadido el número indicado.

        Retorna una nueva lista que incluye el número insertado.
    '''
        
    long= len(lista)

    if lista[long-1] < num:
        lista.append(num)

    else:
        for i in range(long):
            if lista[i] > num:
                lista.insert(i, num)
                break

    return lista


while True:
    try:
        lista = [int(x) for x in input('Ingrese una lista de números enteros'
                                   ':\n').split()]
        if lista == []: print ('Ingresó la lista vacía.')    
        else: break
    except ValueError:
        print('La lista debe contener solo números enteros.')
  
      
# Se verifica si la lista está ordenada o no. En caso de estar ordenada, se 
# ejecuta la función que añade un número ingresado por el usuario y se imprime 
# el resultado. 
    
orden= verificar_orden(len(lista), lista)

if orden != 0 : 
    print ('\nLa lista ingresada no se encuentra ordenada.')

else: # orden == 0
    print ('\nLa lista se encuentra ordenada.')
    while True:
        try:
            num= float(input('Ingrese el número que desea añadir: '))
            break
        except ValueError:
            print('Por favor ingrese un número.')
    
    lista_nueva= anadir_numero(num, lista)

    print ('\nLa nueva lista es: ', end='')
    print (*lista_nueva, sep=', ', end='.')