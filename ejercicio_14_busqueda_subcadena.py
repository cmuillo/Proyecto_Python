"""
Ejercicio 14: Búsqueda de Subcadena

Realice una función que determine si una subcadena (string) existe dentro de otra
sin utilizar funciones nativas como 'in'.

Entrada: Texto principal y subcadena
Proceso: Comparación manual
Salida: True/False
"""

def buscar_subcadena_v1(texto_principal, subcadena):
    """
    Busca si una subcadena existe en el texto principal.
    Versión 1: Usando índices y bucles anidados.
    
    Lógica:
    1. Itera sobre cada posición del texto principal
    2. Compara caracteres uno por uno entre la subcadena y el texto
    3. Si encuentra una coincidencia en todos los caracteres, retorna True
    4. Si termina el bucle sin encontrar, retorna False
    
    
    Args:
        texto_principal (str): El texto donde buscar
        subcadena (str): La cadena a buscar
        
    Returns:
        bool: True si la subcadena existe, False en caso contrario
    """
    # Manejo de casos especiales
    if len(subcadena) == 0:
        # Una subcadena vacía siempre existe
        return True
    
    if len(subcadena) > len(texto_principal):
        # Si la subcadena es más larga que el texto, no puede existir
        return False
    
    # Recorremos el texto principal
    # El rango limita las posiciones donde la subcadena puede empezar
    # Si textos tiene 10 caracteres y buscamos una subcadena de 3,
    # solo hay 8 posiciones posibles (0 a 7) donde puede empezar
    for i in range(len(texto_principal) - len(subcadena) + 1):
        # Asumimos que encontramos la coincidencia
        encontrado = True
        
        # Comparamos cada carácter de la subcadena
        for j in range(len(subcadena)):
            # Si los caracteres no coinciden, no encontramos la subcadena
            if texto_principal[i + j] != subcadena[j]:
                encontrado = False
                break
        
        # Si encontramos una coincidencia completa, retornamos True
        if encontrado:
            return True
    
    # Si recorrimos todo sin encontrar, retornamos False
    return False

    """
    Busca si una subcadena existe en el texto principal.
    Versión 2: Usando slicing (rebandinado) de strings.
    
    Lógica:
    1. Extrae segmentos de tamaño igual a la subcadena del texto principal
    2. Compara cada segmento con la subcadena
    3. Si encuentra una coincidencia, retorna True
    4. Si no encuentra, retorna False
    
    Nota: El slicing en Python es muy optimizado en C, es más rápido.
    Complejidad: O(n*m) pero con mejor rendimiento que la versión 1
    
    Args:
        texto_principal (str): El texto donde buscar
        subcadena (str): La cadena a buscar
        
    Returns:
        bool: True si la subcadena existe, False en caso contrario
    """
    # Manejo de casos especiales
    if len(subcadena) == 0:
        return True
    
    if len(subcadena) > len(texto_principal):
        return False
    
    # Recorremos posiciones posibles
    for i in range(len(texto_principal) - len(subcadena) + 1):
        # Usamos slicing: texto_principal[i:i+len(subcadena)]
        # Extrae una porción del texto del tamaño de la subcadena
        if texto_principal[i:i + len(subcadena)] == subcadena:
            return True
    
    return False



    """
    Busca si una subcadena existe en el texto principal.
    Versión 3: Usando conversión a lista (para comparación más clara).
    
    Lógica:
    Similar a versión 1, pero convierte a listas para mejor visualización
    
    Args:
        texto_principal (str): El texto donde buscar
        subcadena (str): La cadena a buscar
        
    Returns:
        bool: True si la subcadena existe, False en caso contrario
    """
    # Convertimos a listas de caracteres
    texto_lista = list(texto_principal)
    sub_lista = list(subcadena)
    
    if len(sub_lista) == 0:
        return True
    
    if len(sub_lista) > len(texto_lista):
        return False
    
    # Recorremos y comparamos
    for i in range(len(texto_lista) - len(sub_lista) + 1):
        # Extraemos una ventana de caracteres
        ventana = texto_lista[i:i + len(sub_lista)]
        
        # Comparamos si la ventana es igual a la subcadena
        if ventana == sub_lista:
            return True
    
    return False


def imprimir_resultado(texto, subcadena, resultado):
    """
    Imprime el resultado de una búsqueda de forma clara y visual.
    
    Args:
        texto (str): Texto completo
        subcadena (str): Subcadena buscada
        resultado (bool): Resultado de la búsqueda
    """
    estado = "✅ ENCONTRADA" if resultado else "❌ NO ENCONTRADA"
    print(f"Texto: '{texto}'")
    print(f"Buscando: '{subcadena}'")
    print(f"Resultado: {estado}\n")


# ============================================================================
# PRUEBAS
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("BÚSQUEDA DE SUBCADENA (SIN USAR 'in')".center(60))
    print("=" * 60)
    
    # Caso de prueba 1: Subcadena al inicio
    print("\n📌 CASO 1: Subcadena al inicio")
    texto1 = "Esto es una prueba de búsqueda"
    sub1 = "prueba"
    resultado1 = buscar_subcadena_v1(texto1, sub1)
    imprimir_resultado(texto1, sub1, resultado1)
    
  
    