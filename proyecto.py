"""
Sistema de Gestión de Visitantes
Aplicación de consola para registrar y gestionar visitas a un edificio o residencial

Este programa permite gestionar de manera eficiente las visitas registradas en un edificio,
incluyendo información del visitante, vehículo, estado de visita y reportería avanzada.
"""

# ============================================================================
# VARIABLES GLOBALES
# ============================================================================
# Lista que almacena todos los registros de visitas en formato de diccionarios
# Cada diccionario contiene información completa de una visita
visitas = []

# Contador que genera IDs únicos para cada nueva visita registrada
# Se incrementa automáticamente cada vez que se registra una visita
contador_visitas = 0


# ============================================================================
# FUNCIONES DE INTERFAZ (Menús y Presentación)
# ============================================================================

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola imprimiendo líneas en blanco.
    Proporciona una interfaz limpia al usuario (compatible con Windows).
    Nota: En sistemas Unix se podría usar os.system('clear')
    """
    print("\n" * 50)


def mostrar_menu_principal():
    """
    Muestra el menú principal con todas las opciones disponibles.
    Permite al usuario seleccionar qué operación desea realizar en el sistema.
    Las opciones incluyen:
    - Registro de nuevas visitas
    - Consultas de visitas
    - Modificación y cancelación de visitas
    - Control de entrada/salida
    - Reportería y análisis
    """
    print("\n" + "=" * 60)
    print("SISTEMA DE GESTIÓN DE VISITANTES".center(60))
    print("=" * 60)
    print("1. Registrar nueva visita")
    print("2. Consultar todas las visitas")
    print("3. Modificar una visita")
    print("4. Cancelar/Eliminar una visita")
    print("5. Registrar entrada de visitante")
    print("6. Registrar salida de visitante")
    print("7. Reportería y consultas especiales")
    print("8. Salir")
    print("=" * 60)


# ============================================================================
# FUNCIONES DE GENERACIÓN DE ID
# ============================================================================

def obtener_id_visita():
    """
    Genera un ID único e incremental para cada nueva visita registrada.
    
    Funcionamiento:
    - Utiliza la variable global 'contador_visitas' para mantener el contador
    - Cada vez que se llama, incrementa el contador y retorna el nuevo ID
    - Garantiza que cada visita tenga un identificador único
    
    Retorna:
        int: El siguiente ID disponible para una nueva visita
    """
    global contador_visitas
    contador_visitas += 1
    return contador_visitas


# ============================================================================
# FUNCIONES DE REGISTRO Y ENTRADA DE DATOS
# ============================================================================

def registrar_visita():
    """
    Registra una nueva visita en el sistema capturando toda la información requerida.
    
    Proceso:
    1. Solicita datos del visitante (nombre, identificación, destino, motivo, horarios)
    2. Valida que todos los datos sean obligatorios
    3. Pregunta si el visitante ingresa con vehículo
    4. Si hay vehículo, captura datos del mismo (placa, marca, modelo, color, tipo)
    5. Crea un diccionario con toda la información
    6. Agrupa el registro a la lista global de visitas
    7. Muestra confirmación con el ID asignado
    
    La función usa validación básica para asegurar que no se registren datos vacíos
    y crea un nuevo ID único para cada visita mediante obtener_id_visita()
    """
    print("\n--- REGISTRO DE NUEVA VISITA ---")
    
    # ============ CAPTURA DE DATOS DEL VISITANTE ============
    # Se solicitan los datos personales del visitante que desea ingresar al edificio
    nombre = input("Nombre del visitante: ").strip()
    if not nombre:
        print("❌ El nombre es obligatorio.")
        return
    
    # La identificación puede ser cédula, TIM, pasaporte, etc.
    identificacion = input("Número de identificación (cédula, TIM, Pasaporte): ").strip()
    if not identificacion:
        print("❌ La identificación es obligatoria.")
        return
    
    # Apartamento, casa o unidad a la que se dirige el visitante
    apartamento = input("Apartamento, casa o unidad a la que se dirige: ").strip()
    if not apartamento:
        print("❌ La unidad destino es obligatoria.")
        return
    
    # Motivo de la visita (reunión, entrega, visita social, etc.)
    motivo = input("Motivo de la visita: ").strip()
    if not motivo:
        print("❌ El motivo es obligatorio.")
        return
    
    # Hora planeada de entrada en formato HH:MM
    hora_entrada = input("Hora planeada de entrada (ej: 14:30): ").strip()
    if not hora_entrada:
        print("❌ La hora de entrada es obligatoria.")
        return
    
    # Hora planeada de salida en formato HH:MM
    hora_salida = input("Hora planeada de salida (ej: 15:30): ").strip()
    if not hora_salida:
        print("❌ La hora de salida es obligatoria.")
        return
    
    # ============ CAPTURA DE DATOS DEL VEHÍCULO (OPCIONAL) ============
    # Se pregunta si el visitante ingresa con vehículo
    con_vehiculo = input("¿El visitante ingresa con vehículo? (S/N): ").upper()
    datos_vehiculo = None
    
    # Si llegó con vehículo, se capturan los datos del mismo
    if con_vehiculo == "S":
        placa = input("Placa del vehículo: ").strip()
        marca = input("Marca del vehículo: ").strip()
        modelo = input("Modelo del vehículo: ").strip()
        color = input("Color del vehículo: ").strip()
        tipo = input("Tipo de vehículo (automóvil, motocicleta, etc): ").strip()
        
        # Se crea un diccionario con toda la información del vehículo
        datos_vehiculo = {
            "placa": placa,
            "marca": marca,
            "modelo": modelo,
            "color": color,
            "tipo": tipo
        }
    
    # ============ CREACIÓN DEL REGISTRO DE VISITA ============
    # Se crea un diccionario con todos los datos de la visita
    # Este diccionario contiene todos los campos necesarios para registrar completamente una visita
    visita = {
        "id": obtener_id_visita(),              # ID único generado automáticamente
        "nombre": nombre,                        # Nombre del visitante
        "identificacion": identificacion,        # Documento de identificación
        "apartamento": apartamento,              # Unidad destino del visitante
        "motivo": motivo,                        # Razón de la visita
        "hora_entrada": hora_entrada,            # Hora planeada de ingreso
        "hora_salida": hora_salida,              # Hora planeada de salida
        # Estados posibles: "pendiente" (sin ingresar), "dentro" (ya ingresó),
        # "finalizada" (ya salió), "cancelada" (visita cancelada)
        "estado": "pendiente",
        "vehiculo": datos_vehiculo,              # Datos del vehículo (si aplica)
        "con_vehiculo": con_vehiculo == "S"      # Bandera booleana: ¿tiene vehículo?
    }
    
    # Se agrega el nuevo registro a la lista global de visitas
    visitas.append(visita)
    print(f"\n✅ Visita registrada exitosamente con ID: {visita['id']}")


# ============================================================================
# FUNCIONES DE CONSULTA Y BÚSQUEDA
# ============================================================================

def consultar_todas_visitas():
    """
    Muestra en formato tabulado todos los registros de visitas actualmente en el sistema.
    
    Características:
    - Verifica que existan visitas registradas
    - Itera sobre la lista de visitas mostrando toda la información relevante
    - Si hay vehículo, muestra los datos del mismo (marca, modelo, color, placa)
    - Si no hay vehículo, solo muestra "No"
    - Proporciona una vista completa para supervisión y auditoría
    """
    if not visitas:
        print("\n❌ No hay visitas registradas en el sistema.")
        return
    
    print("\n" + "=" * 100)
    print("LISTA DE VISITAS REGISTRADAS".center(100))
    print("=" * 100)
    
    # Itera sobre cada visita en la lista global
    for visita in visitas:
        print(f"\nID: {visita['id']}")
        print(f"  Visitante: {visita['nombre']}")
        print(f"  Identificación: {visita['identificacion']}")
        print(f"  Unidad destino: {visita['apartamento']}")
        print(f"  Motivo: {visita['motivo']}")
        print(f"  Hora entrada: {visita['hora_entrada']}")
        print(f"  Hora salida: {visita['hora_salida']}")
        print(f"  Estado: {visita['estado']}")
        print(f"  Con vehículo: {'Sí' if visita['con_vehiculo'] else 'No'}", end="")
        
        # Si el registro includes information about a vehicle, displays its details
        if visita['vehiculo']:
            veh = visita['vehiculo']
            print(f" - {veh['marca']} {veh['modelo']} ({veh['color']}) - Placa: {veh['placa']}")
        else:
            print()
    
    print("\n" + "=" * 100)


def buscar_visita_por_id():
    """
    Busca una visita específica en la lista usando su ID único.
    
    Proceso:
    1. Solicita al usuario ingresar el ID de la visita que desea buscar
    2. Valida que la entrada sea un número
    3. Itera sobre la lista de visitas comparando los IDs
    4. Retorna la visita si la encuentra, None si no existe
    5. Muestra mensaje de error en casos de ID inválido o no encontrado
    
    Retorna:
        dict: El diccionario de la visita encontrada, o None si no existe
    """
    try:
        id_visita = int(input("Ingrese el ID de la visita: "))
        # Recorre todas las visitas buscando coincidencia de ID
        for visita in visitas:
            if visita['id'] == id_visita:
                return visita
        print(f"❌ No se encontró visita con ID {id_visita}")
        return None
    except ValueError:
        print("❌ ID inválido. Debe ser un número.")
        return None


# ============================================================================
# FUNCIONES DE MODIFICACIÓN Y EDICIÓN
# ============================================================================

def modificar_visita():
    """
    Permite actualizar la información de una visita registrada.
    
    Restricciones:
    - No se puede modificar una visita que ya ha sido "finalizada"
    - Se pueden modificar: motivo, horarios, unidad destino, datos del vehículo
    
    Proceso:
    1. Busca la visita por ID
    2. Valida que la visita no esté finalizada
    3. Muestra un submenú con opciones de modificación
    4. Actualiza el campo seleccionado
    5. Confirma la actualización al usuario
    
    Las validaciones previenen cambios en visitas completadas o canceladas.
    """
    visita = buscar_visita_por_id()
    if not visita:
        return
    
    # Validación: no permite modificar visitas finalizadas
    if visita['estado'] == "finalizada":
        print("❌ No se puede modificar una visita que ya ha finalizado.")
        return
    
    print("\n--- MODIFICAR VISITA ---")
    print("¿Qué desea modificar?")
    print("1. Motivo de la visita")
    print("2. Horario planeado")
    print("3. Unidad destino")
    print("4. Información del vehículo")
    print("5. Cancelar")
    
    opcion = input("Seleccione opción: ").strip()
    
    # OPCIÓN 1: Modificar motivo de la visita
    if opcion == "1":
        nuevo_motivo = input("Nuevo motivo de la visita: ").strip()
        if nuevo_motivo:
            visita['motivo'] = nuevo_motivo
            print("✅ Motivo actualizado.")
    
    # OPCIÓN 2: Modificar horarios (entrada y salida)
    elif opcion == "2":
        nueva_entrada = input("Nueva hora de entrada (ej: 14:30): ").strip()
        nueva_salida = input("Nueva hora de salida (ej: 15:30): ").strip()
        if nueva_entrada and nueva_salida:
            visita['hora_entrada'] = nueva_entrada
            visita['hora_salida'] = nueva_salida
            print("✅ Horario actualizado.")
    
    # OPCIÓN 3: Modificar unidad destino
    elif opcion == "3":
        nueva_unidad = input("Nueva unidad destino: ").strip()
        if nueva_unidad:
            visita['apartamento'] = nueva_unidad
            print("✅ Unidad destino actualizada.")
    
    # OPCIÓN 4: Modificar información del vehículo
    elif opcion == "4":
        # Primero verifica que la visita tenga registrado un vehículo
        if visita['con_vehiculo']:
            print("¿Qué datos del vehículo desea actualizar?")
            print("1. Placa")
            print("2. Marca")
            print("3. Modelo")
            print("4. Color")
            print("5. Tipo")
            
            sub_opcion = input("Seleccione campo: ").strip()
            
            # Actualiza el campo específico del vehículo
            if sub_opcion == "1":
                visita['vehiculo']['placa'] = input("Nueva placa: ").strip()
                print("✅ Placa actualizada.")
            elif sub_opcion == "2":
                visita['vehiculo']['marca'] = input("Nueva marca: ").strip()
                print("✅ Marca actualizada.")
            elif sub_opcion == "3":
                visita['vehiculo']['modelo'] = input("Nuevo modelo: ").strip()
                print("✅ Modelo actualizado.")
            elif sub_opcion == "4":
                visita['vehiculo']['color'] = input("Nuevo color: ").strip()
                print("✅ Color actualizado.")
            elif sub_opcion == "5":
                visita['vehiculo']['tipo'] = input("Nuevo tipo: ").strip()
                print("✅ Tipo actualizado.")
        else:
            print("❌ Esta visita no registró vehículo.")


# ============================================================================
# FUNCIONES DE GESTIÓN DE ESTADO (Entrada, Salida, Cancelación)
# ============================================================================

def cancelar_eliminar_visita():
    """
    Marca una visita como "cancelada" en el sistema.
    
    Características:
    - Busca la visita por ID
    - Valida que no esté ya finalizada (pues una visita finalizada no puede cancelarse)
    - Solicita confirmación al usuario antes de cancelar
    - Cambia el estado de la visita a "cancelada"
    
    Nota: No elimina la visita de la base de datos, solo marca su estado.
    Esto es importante para auditoría y reportes posteriores.
    """
    visita = buscar_visita_por_id()
    if not visita:
        return
    
    # Validación: no permite cancelar visitas que ya finalizaron
    if visita['estado'] == "finalizada":
        print("❌ No se puede cancelar una visita que ya ha finalizado.")
        return
    
    # Solicita confirmación para evitar cancelaciones accidentales
    confirmacion = input(f"¿Confirma la cancelación de la visita de {visita['nombre']}? (S/N): ").upper()
    
    if confirmacion == "S":
        confirmacion = input(f"¿Realmente desea la cancelación de la visita de {visita['nombre']}? (S/N): ").upper()
        if confirmacion == "S":
            visita['estado'] = "cancelada"
            print("✅ Visita cancelada exitosamente.")
        else:
            print("❌ Operación cancelada.")
    else:
        print("❌ Operación cancelada.")


def registrar_entrada_visitante():
    """
    Marca que un visitante ha ingresado al edificio.
    
    Funcionamiento:
    1. Busca la visita por ID
    2. Valida que no esté finalizada ni cancelada
    3. Cambia el estado a "dentro"
    4. Registra que el visitante está actualmente dentro
    
    Estados permitidos para cambiar a "dentro":
    - "pendiente" (primera vez que ingresa)
    
    Estados que NO permiten cambio:
    - "finalizada" (ya salió)
    - "cancelada" (visita cancelada)
    """
    visita = buscar_visita_por_id()
    if not visita:
        return
    
    if visita['estado'] == "finalizada":
        print("❌ Esta visita ya ha finalizado.")
        return
    
    if visita['estado'] == "cancelada":
        print("❌ Esta visita ha sido cancelada.")
        return
    
    # Marca el estado como "dentro" y confirma al usuario
    visita['estado'] = "dentro"
    print(f"✅ {visita['nombre']} ha ingresado al edificio. Estado: DENTRO")


def registrar_salida_visitante():
    """
    Marca que un visitante ha salido del edificio finalizando la visita.
    
    Funcionamiento:
    1. Busca la visita por ID
    2. Valida que esté en estado "dentro" (actualmente dentro del edificio)
    3. Cambia el estado a "finalizada"
    4. Registra la hora de salida
    
    Validación importante:
    - Solo se puede registrar salida si la visita está en estado "dentro"
    - Impide errores de registro (ejm. registrar salida de visitante que aún no ingresó)
    """
    visita = buscar_visita_por_id()
    if not visita:
        return
    
    # Valida que el visitante esté dentro para poder salir
    if visita['estado'] != "dentro":
        print("❌ Esta visita no está marcada como 'dentro' del edificio.")
        return
    
    visita['estado'] = "finalizada"
    print(f"✅ {visita['nombre']} ha salido del edificio. Visita finalizada.")


# ============================================================================
# FUNCIONES DE REPORTERÍA Y ANÁLISIS
# ============================================================================

def mostrar_menu_reporteria():
    """
    Muestra el menú de opciones para reportería y consultas especializadas.
    
    Opciones disponibles:
    1. Visitantes actualmente dentro del edificio (en tiempo real)
    2. Visitantes que registraron vehículo
    3. Todas las visitas para una unidad específica
    4. Resumen estadístico de visitas por estado
    5. Volver al menú principal
    """
    print("\n" + "=" * 60)
    print("REPORTERÍA Y CONSULTAS ESPECIALES".center(60))
    print("=" * 60)
    print("1. Visitantes actualmente dentro del edificio")
    print("2. Visitantes que ingresaron con vehículo")
    print("3. Visitas para un apartamento específico")
    print("4. Resumen de visitas por estado")
    print("5. Volver al menú principal")
    print("=" * 60)


def visitantes_dentro_edificio():
    """
    Muestra todos los visitantes que actualmente se encuentran dentro del edificio.
    
    Funcionamiento:
    - Utiliza una comprensión de lista (list comprehension) para filtrar visitas
    - Busca solo visitas con estado = "dentro"
    - Muestra información clave: nombre, ID, identificación, unidad, motivo, hora entrada
    - Útil para supervisión en tiempo real
    
    Datos mostrados:
    - Nombre del visitante
    - ID de la visita
    - Documento de identificación
    - Unidad a la que accede
    - Motivo de la visita
    - Hora de ingreso
    """
    # Filtra solo las visitas que están "dentro" del edificio
    visitantes_activos = [v for v in visitas if v['estado'] == "dentro"]
    
    if not visitantes_activos:
        print("\n✅ No hay visitantes dentro del edificio en este momento.")
        return
    
    print("\n" + "=" * 80)
    print("VISITANTES ACTUALMENTE DENTRO DEL EDIFICIO".center(80))
    print("=" * 80)
    
    # Muestra detalles de cada visitante activo
    for visita in visitantes_activos:
        print(f"\n  {visita['nombre']} (ID: {visita['id']})")
        print(f"  Identificación: {visita['identificacion']}")
        print(f"  Unidad: {visita['apartamento']}")
        print(f"  Motivo: {visita['motivo']}")
        print(f"  Hora entrada: {visita['hora_entrada']}")
    
    print("\n" + "=" * 80)


def visitantes_con_vehiculo():
    """
    Muestra todos los visitantes que ingresaron con vehículo.
    
    Funcionamiento:
    - Utiliza list comprehension para filtrar solo visitas con vehículo
    - Busca visitas donde con_vehiculo = True
    - Muestra información del vehículo: marca, modelo, color, placa, tipo
    - Útil para control de estacionamiento y seguridad
    
    Información mostrada:
    - Datos del visitante (nombre, identificación)
    - Datos completos del vehículo
    - Unidad a la que accede
    - Estado actual de la visita
    """
    # Filtra solo las visitas que registran vehículo
    with_vehicle = [v for v in visitas if v['con_vehiculo']]
    
    if not with_vehicle:
        print("\n✅ No hay visitantes registrados con vehículo.")
        return
    
    print("\n" + "=" * 100)
    print("VISITANTES QUE INGRESARON CON VEHÍCULO".center(100))
    print("=" * 100)
    
    # Itera y muestra información de cada visitante con vehículo
    for visita in with_vehicle:
        veh = visita['vehiculo']
        print(f"\n  Visitante: {visita['nombre']}")
        print(f"  Identificación: {visita['identificacion']}")
        print(f"  Vehículo: {veh['marca']} {veh['modelo']} ({veh['color']})")
        print(f"  Placa: {veh['placa']}")
        print(f"  Tipo: {veh['tipo']}")
        print(f"  Unidad: {visita['apartamento']}")
        print(f"  Estado: {visita['estado']}")
    
    print("\n" + "=" * 100)


def visitas_por_apartamento():
    """
    Muestra todas las visitas registradas para una unidad específica.
    
    Funcionamiento:
    1. Solicita al usuario ingresar el número/identificación del apartamento
    2. Utiliza list comprehension con comparación case-insensitive
    3. Muestra todas las visitas (pasadas y presentes) para esa unidad
    4. Útil para auditar quién ha visitado una unidad específica
    
    Dato mostrado:
    - ID, visitante, identificación, motivo, horarios y estado
    """
    # Solicita el apartamento a filtrar
    apartamento = input("Ingrese el apartamento/unidad: ").strip()
    
    # Busca todas las visitas para ese apartamento (case-insensitive)
    visitas_unidad = [v for v in visitas if v['apartamento'].lower() == apartamento.lower()]
    
    if not visitas_unidad:
        print(f"\n✅ No hay visitas registradas para la unidad {apartamento}.")
        return
    
    print(f"\n" + "=" * 80)
    print(f"VISITAS PARA LA UNIDAD {apartamento.upper()}".center(80))
    print("=" * 80)
    
    # Muestra cada visita para la unidad
    for visita in visitas_unidad:
        print(f"\n  ID: {visita['id']}")
        print(f"  Visitante: {visita['nombre']}")
        print(f"  Identificación: {visita['identificacion']}")
        print(f"  Motivo: {visita['motivo']}")
        print(f"  Hora entrada: {visita['hora_entrada']}")
        print(f"  Hora salida: {visita['hora_salida']}")
        print(f"  Estado: {visita['estado']}")
    
    print("\n" + "=" * 80)


def resumen_por_estado():
    """
    Muestra un resumen estadístico de todas las visitas agrupadas por estado.
    
    Funcionamiento:
    - Crea un diccionario con los 4 posibles estados: pendiente, dentro, finalizada, cancelada
    - Itera sobre todas las visitas incrementando el contador del estado correspondiente
    - Muestra el total de visitas por estado y el total general
    
    Estados contabilizados:
    - Pendiente: Visitas registradas pero aún no ingresaron
    - Dentro: Visitantes actualmente dentro del edificio
    - Finalizada: Visitas completadas (visitante ya salió)
    - Cancelada: Visitas que fueron canceladas
    
    Utilidad: Proporciona una visión rápida del estado del sistema
    """
    # Crea diccionario para contabilizar visitas por estado
    estados = {"pendiente": 0, "dentro": 0, "finalizada": 0, "cancelada": 0}
    
    # Itera sobre todas las visitas y cuenta por estado
    for visita in visitas:
        estados[visita['estado']] += 1
    
    print("\n" + "=" * 60)
    print("RESUMEN DE VISITAS POR ESTADO".center(60))
    print("=" * 60)
    print(f"Pendientes:  {estados['pendiente']}")
    print(f"Dentro:      {estados['dentro']}")
    print(f"Finalizadas: {estados['finalizada']}")
    print(f"Canceladas:  {estados['cancelada']}")
    print(f"Total:       {len(visitas)}")
    print("=" * 60)


def menu_reporteria():
    """
    Gestiona el menú de reportería con un bucle interactivo.
    
    Funcionamiento:
    - Muestra el menú de reportería
    - Captura la opción del usuario
    - Ejecuta la función correspondiente
    - Repite hasta que el usuario seleccione salir (opción 5)
    
    Este es un ejemplo de un submenú que permite acceder a funciones
    especializadas sin volver al menú principal después de cada operación.
    """
    while True:
        mostrar_menu_reporteria()
        opcion = input("Seleccione opción: ").strip()
        
        # Ejecuta la función correspondiente según la opción
        if opcion == "1":
            visitantes_dentro_edificio()
        elif opcion == "2":
            visitantes_con_vehiculo()
        elif opcion == "3":
            visitas_por_apartamento()
        elif opcion == "4":
            resumen_por_estado()
        elif opcion == "5":
            break  # Sale del bucle y vuelve al menú principal
        else:
            print("❌ Opción no válida.")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que controla el flujo del programa.
    
    Funcionamiento:
    1. Muestra un mensaje de bienvenida
    2. Entra en un bucle infinito que:
       - Muestra el menú principal
       - Captura la opción del usuario
       - Ejecuta la función correspondiente
       - Solicita al usuario presionar ENTER para continuar
    3. Sale cuando el usuario selecciona opción 8 (Salir)
    
    Estructura de flujo:
    - Esta es la función que se ejecuta cuando se inicia el programa
    - Actúa como un controlador central dirigiendo a todas las demás funciones
    - Mantiene el programa en ejecución hasta que el usuario decida salir
    
    El bucle while True con break asegura que el programa continúe
    sólo si el usuario no selecciona salir.
    """
    # Muestra un mensaje de bienvenida al inicio
    print("\n" + "=" * 60)
    print("BIENVENIDO AL SISTEMA DE GESTIÓN DE VISITANTES".center(60))
    print("=" * 60)
    
    # Bucle principal que mantiene el programa en ejecución
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        
        # Opción 1: Registrar nueva visita
        if opcion == "1":
            registrar_visita()
        
        # Opción 2: Consultar todas las visitas
        elif opcion == "2":
            consultar_todas_visitas()
        
        # Opción 3: Modificar una visita existente
        elif opcion == "3":
            modificar_visita()
        
        # Opción 4: Cancelar o eliminar una visita
        elif opcion == "4":
            cancelar_eliminar_visita()
        
        # Opción 5: Registrar entrada del visitante
        elif opcion == "5":
            registrar_entrada_visitante()
        
        # Opción 6: Registrar salida del visitante
        elif opcion == "6":
            registrar_salida_visitante()
        
        # Opción 7: Acceder a reportería y consultas especiales
        elif opcion == "7":
            menu_reporteria()
        
        # Opción 8: Salir del programa
        elif opcion == "8":
            print("\n✅ ¡Gracias por usar el sistema! Hasta pronto.")
            break  # Sale del bucle while y finaliza el programa
        
        # Opción no válida
        else:
            print("\n❌ Opción no válida. Intente de nuevo.")
        
        # Pausa antes de volver al menú principal
        input("\nPresione ENTER para continuar...")


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    """
    Bloque de punto de entrada estándar de Python.
    
    Significado:
    - 'if __name__ == "__main__"' es una convención de Python
    - Se ejecuta solo si el script se ejecuta directamente
    - NO se ejecuta si el script es importado como módulo en otro programa
    - Permite usar este código tanto como programa ejecutable como librería importable
    
    En este caso, simplemente llama a la función main() para iniciar el programa.
    """
    main()
