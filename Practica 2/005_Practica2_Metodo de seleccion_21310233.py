# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Practica 2
Metodos de Ordenamiento
Metodo de seleccion
"""

def selection_sort(lista):
    # Iteramos sobre cada elemento de la lista
    for i in range(len(lista)):
        # Suponemos que el primer elemento de la porción no ordenada es el menor
        min_index = i
        # Iteramos sobre la porción no ordenada
        for j in range(i + 1, len(lista)):
            # Si encontramos un elemento menor, actualizamos min_index
            if lista[j] < lista[min_index]:
                min_index = j
        # Intercambiamos el elemento actual con el elemento más pequeño encontrado
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Programa principal para demostrar el uso del algoritmo de ordenación por selección
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [64, 25, 12, 22, 11]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo de ordenación por selección
    lista_ordenada = selection_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()