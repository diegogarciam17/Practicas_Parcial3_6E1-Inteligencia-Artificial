# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Practica 2
Metodos de Ordenamiento
Metodo de burbuja
"""

def bubble_sort(lista):
    # Obtenemos el tamaño de la lista
    n = len(lista)
    
    # Iteramos sobre cada elemento de la lista
    for i in range(n):
        # Inicializamos una bandera que indica si hubo algún intercambio
        intercambio = False
        
        # Iteramos sobre la lista desde el inicio hasta el penúltimo elemento no ordenado
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Indicamos que hubo un intercambio
                intercambio = True
        
        # Si no hubo intercambios en la iteración, la lista ya está ordenada
        if not intercambio:
            break
    
    return lista

# Programa principal para demostrar el uso del algoritmo de ordenación por burbuja
def main():
    # Ejemplo de lista desordenada
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
    print("Lista desordenada:", lista_desordenada)

    # Ordenamos la lista utilizando el algoritmo de ordenación por burbuja
    lista_ordenada = bubble_sort(lista_desordenada)
    print("Lista ordenada:", lista_ordenada)

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()