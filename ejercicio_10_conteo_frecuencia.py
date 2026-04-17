"""
Ejercicio 10: Conteo de Frecuencia

Realice una función que cuente cuántas veces aparece cada elemento dentro de una lista.

Entrada: Lista
Proceso: Recorrido y acumulación
Salida: Impresión de ocurrencias
"""

def contar_frecuencia(lista):
    """
    Cuenta cuántas veces aparece cada elemento en una lista.
    
    Lógica:
    1. Crea un diccionario vacío para almacenar los elementos y sus conteos
    2. Recorre cada elemento de la lista
    3. Si el elemento ya existe en el diccionario, incrementa su contador
    4. Si es la primera vez que ve el elemento, lo agrega con contador = 1
    5. Retorna el diccionario con los conteos
    

    Args:
        lista: Una lista con elementos para contar
        
    Returns:
        dict: Diccionario con {elemento: cantidad de ocurrencias}
    """
    # Diccionario para almacenar los conteos de cada elemento
    frecuencias = {}
    
    # Recorremos cada elemento en la lista
    for elemento in lista:
        # Si el elemento ya existe en el diccionario, incrementamos su contador
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            # Si es la primera vez que vemos este elemento, lo agregamos con valor 1
            frecuencias[elemento] = 1
    
    return frecuencias


def imprimir_frecuencias(lista):
    """
    Cuenta y muestra las frecuencias de cada elemento en una lista.
    Imprime de forma clara y legible.
    
    Args:
        lista: Una lista con elementos para contar
    """
    frecuencias = contar_frecuencia(lista)
    
    print("\n" + "=" * 50)
    print("CONTEO DE FRECUENCIA".center(50))
    print("=" * 50)
    print(f"Lista original: {lista}\n")
    
    for elemento, cantidad in frecuencias.items():
        print(f"'{elemento}': aparece {cantidad} vez{'ces' if cantidad > 1 else ''}")
    
    print("\n" + "=" * 50)


# ============================================================================
# PRUEBAS
# ============================================================================

if __name__ == "__main__":
    # Ejemplo 1: Lista de números
    lista_numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    print("\n📊 EJERCICIO 10: Conteo de frecuencias")
    imprimir_frecuencias(lista_numeros)

