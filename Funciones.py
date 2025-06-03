import os


# Funciones del programa -> 

def init_matriz(cantidad_filas:int = 2, cantidad_columnas:int = 3,valor_inicial:any = 0) -> list:
    """Inizialización de la Matriz

    Args:
        cantidad_filas (int, optional): Defaults to 2.
        cantidad_columnas (int, optional): Defaults to 3.
        valor_inicial (any, optional): Defaults to 0.

    Returns:
        list: Matriz inicializada
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz += [fila]
        
    return matriz

def registrar_participantes(participantes:list) -> list:
    """Registración de los Participantes del certamen

    Args:
        participantes (list): lista de participantes inicial

    Returns:
        list: lista con los registros agregados.
    """
        
    while True: 
        os.system("clear")
        print("     -> (1) Ingrese un nuevo participante\n     -> (0) Volver al menú anterior. ")
        user_input = pedir_dato("\nElegí una opción para proceder: ", int, 0, 1)
      
        match user_input:
            case 1: 
                os.system("clear")
                nombre_participante = pedir_dato("-> Ingrese el nombre del participante: ", str, 0, 3)
                participantes = participantes + [nombre_participante]
            case 0:
                break
        
    return participantes

def definir_matriz(matriz, participantes:list, jurados:int = 3) -> list:
    """Define las filas y columnas de nuestra matriz para almacenar los datos necesarios. 
       Los participantes seran referidos en la lista participantes = [].
       Cada indice de esta fila coincidirá con los indices de las filas de la Matriz. 
       Cada columna representará a los jurados.
       Los valores almacenados serán el valor de los votos.  

    Args:
        matriz (list): Matriz de referencia
        participantes (list): _description_
        jurados (int, optional): _description_. Defaults to 3.
        
    Returns: 
        matriz (list): Matriz con filas y columnas adecuadas.
    """
    if len(matriz) == 0:
        return init_matriz(len(participantes), jurados)
    
    if len(matriz[0]) < jurados:
        diferencia = jurados - len(matriz[0])
        for i in range(len(matriz)):
            matriz[i] = matriz[i] + [0] * diferencia
    
    if len(matriz) < len(participantes):
        fila = [0] * len(matriz[0])
        for _ in range(len(participantes) - len(matriz)):
            matriz += [fila]
    
    return matriz

def carga_puntuacion(matriz:list, participantes:list, i:int, jurados:int):
    j = 1
    while j <= jurados: 
        nota = pedir_dato(f"JURADO {j}: Ingrese la nota del participante {participantes[i]} : ", int, 0, 10)
        matriz[i][j-1] = nota
        j += 1
        
    print("Notas: ", matriz[i])
    
def get_all_participantes(participantes:list) -> str:
    print("-> Lista de Participantes: \n")
    for i in range(len(participantes)):
        print(i+1, participantes[i])

def buscar_participante(participantes:list, user_input:str) -> str:
    encontrado = False
    for i in range(len(participantes)):
        if participantes[i].lower() == user_input.lower():
            print(f"Participante {participantes[i]} encontrado! Procediendo a la carga de puntuación: ")
            encontrado = True
            return i
    if not encontrado:
        return None

def mostrar_puntuaciones(matriz: list, participantes: list, idx:int, ) -> None:
    idx = idx -1
    if idx < 0 or idx >= len(participantes):
        print("Índice de participante fuera de rango.")
        return
    puntuaciones = matriz[idx]
    print(f" -> Participante: {participantes[idx]}\n Puntuaciones:\n")
    p_sum = 0
    for i in range(len(puntuaciones)):
        print(f"Jurado {i+1}: {puntuaciones[i]}")
        p_sum = p_sum + puntuaciones[i]
    promedio = float(p_sum / len(puntuaciones))
    print(f"Promedio: {promedio}")
    
def mostrar_promedio_mayor(matriz:list, participantes:list, min:int) -> list:
    """Muestra los promedios mayores al {promedio} ingresado

    Args:
        matriz (_type_): 
        participantes (_type_): _description_
        promedio (_type_): _description_
    """
    result = []
    for i in range(len(matriz)):
        p_sum = 0
        for j in range(len(matriz[i])):
            p_sum = p_sum + matriz[i][j]
        promedio = p_sum / len(matriz[i])
        if promedio > min:
            result = result + [participantes[i]]
    return result

def promedios_por_jurado(matriz: list) -> list:
    """Obtenemos los promedios por jurado

    Args:
        matriz (list): Matriz originaria con la que trabajamos todo el codigo.

    Returns:
        list: retorna una lista con los promedios de cada jurado
    """
    if len(matriz) == 0:
        return []     
                     
    promedios = []             

    for j in range(len(matriz[0])):
        p_sum = 0
        for i in range(len(matriz)):
            p_sum = p_sum + matriz[i][j]
        promedio = p_sum / len(matriz)
        promedios = promedios + [promedio]   

    return promedios

def promedios_por_alumno(matriz:list) -> list:
    for i in range(len(matriz)):
        p_sum = 0
        for j in range(len(matriz[0])):
            p_sum = p_sum + matriz[i][j]
        promedio = p_sum / len(matriz[0])
    
    promedios = promedios + [promedio]
    return promedios

## OTRAS FUNCIONES HELPERS -> 

def pedir_dato(mensaje: str, tipo: type = int, minimo: int = None, maximo: int = None, longitud_minima: int = None) -> int | str:
    """
    Lee un valor de la consola y lo valida según los parámetros recibidos.
    - tipo: int  → intenta castear a entero
            str  → deja como string
    - minimo / maximo: límites para enteros
    - longitud_minima: para strings
    - solo_letras: obliga a que el texto contenga solo letras y espacios
    Devuelve el valor ya validado.
    """
    while True:
        dato_ingresado = input(mensaje)

        if tipo is int:
            try:
                valor_int = int(dato_ingresado)
                if minimo is not None and valor_int < minimo:
                    print(f"Debe ser >= {minimo}")
                    continue
                if maximo is not None and valor_int > maximo:
                    print(f"Debe ser <= {maximo}")
                    continue
                return valor_int
            except ValueError:
                print("Ups! Debes ingresar un número entero. Volvé a intentarlo.")
                continue

        elif tipo is str:
            try: 
                valor_str = str(dato_ingresado)    
                if longitud_minima and len(mensaje) < longitud_minima:
                    print(f"Debe tener al menos {longitud_minima} caracteres.")
                    continue
                return valor_str
            except ValueError: 
                print("Ups! El nombre debe contener al menos 3 letras. Volvé a intentarlo.")

def cargar_datos_ejemplo(matriz: list, participantes: list, cant_jurados: int) -> tuple[list, list]:
    """
    Carga automática de participantes y sus puntuaciones para pruebas.
    Utiliza las funciones propias del sistema (sin append, sin copy).

    Returns:
        tuple: participantes y matriz actualizada
    """
    nombres_demo = [
        "Juan Pérez", 
        "María González", 
        "Pedro Ramírez", 
        "Ana Torres", 
        "Luis Fernández"
    ]

    puntajes_demo = [
        [8, 9, 7],
        [6, 5, 7],
        [9, 9, 10],
        [4, 4, 5],
        [7, 6, 7]
    ]

    participantes = []
    for nombre in nombres_demo:
        participantes = participantes + [nombre]

    matriz = definir_matriz(matriz, participantes, cant_jurados)

    for i in range(len(participantes)):
        for j in range(cant_jurados):
            matriz[i][j] = puntajes_demo[i][j]

    print("✅ Datos de ejemplo cargados correctamente.")
    return matriz, participantes
