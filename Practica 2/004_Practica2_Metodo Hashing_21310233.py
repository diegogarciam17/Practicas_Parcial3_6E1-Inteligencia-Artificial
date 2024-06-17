# -*- coding: utf-8 -*-
"""
Diego Ivan Garcia Monteon
21310233    6E1
Inteligencia Artificial
Practica 2
Metodos de Ordenamiento
Metodo Hashing
"""

class HashTable:
    def __init__(self, size):
        # Inicializamos la tabla hash con una lista de listas vacías
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # Calculamos el índice hash utilizando el operador módulo
        return hash(key) % self.size

    def insert(self, key, value):
        # Calculamos el índice hash para la clave
        index = self.hash_function(key)
        # Verificamos si la clave ya existe en la tabla hash
        for kvp in self.table[index]:
            if kvp[0] == key:
                # Si la clave ya existe, actualizamos su valor
                kvp[1] = value
                return
        # Si la clave no existe, agregamos un nuevo par clave-valor
        self.table[index].append([key, value])

    def search(self, key):
        # Calculamos el índice hash para la clave
        index = self.hash_function(key)
        # Buscamos la clave en la lista enlazada correspondiente
        for kvp in self.table[index]:
            if kvp[0] == key:
                # Si encontramos la clave, devolvemos su valor
                return kvp[1]
        # Si no encontramos la clave, devolvemos None
        return None

    def delete(self, key):
        # Calculamos el índice hash para la clave
        index = self.hash_function(key)
        # Buscamos la clave en la lista enlazada correspondiente
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                # Si encontramos la clave, la eliminamos de la lista
                del self.table[index][i]
                return True
        # Si no encontramos la clave, devolvemos False
        return False

# Programa principal para demostrar el uso de la tabla hash
def main():
    # Creamos una tabla hash con un tamaño de 10
    hash_table = HashTable(10)

    # Insertamos algunos pares clave-valor
    hash_table.insert("nombre", "Juan")
    hash_table.insert("edad", 25)
    hash_table.insert("ciudad", "Berlin")

    # Buscamos y mostramos algunos valores
    print("Nombre:", hash_table.search("nombre"))
    print("Edad:", hash_table.search("edad"))
    print("Ciudad:", hash_table.search("ciudad"))

    # Intentamos eliminar una clave
    if hash_table.delete("edad"):
        print("Clave 'edad' eliminada.")
    else:
        print("Clave 'edad' no encontrada.")

    # Intentamos buscar una clave eliminada
    print("Edad después de eliminar:", hash_table.search("edad"))

# Llamamos a la función principal para iniciar el programa
if __name__ == "__main__":
    main()