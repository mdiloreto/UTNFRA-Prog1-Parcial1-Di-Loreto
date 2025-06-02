import os
from Funciones import *

cant_jurados = 3
participantes = [] 
matriz_puntuacion = init_matriz()

while True: 
    os.system("clear")
    print("¡COMPETENCIA ABIERTA DE ACADEMIA DE BAILE! ")
    print(" --- MENU DE OPCIONES: ---\n\n -> (1) Registrar participantes \n -> (2) Registrar puntuaciones del Jurado\n -> (3) Ver información de los Datos cargados\n -> (4) Definir la cantidad de jurados \n -> (0) Salir del programa. \n\n")
    
    # Opcional para Troubleshooting
    print("Lista de Participantes", participantes)
    print("Matriz de puntuaciones", matriz_puntuacion)

    user_input = pedir_dato("   -> Elegí una opción para proceder: ", int, 0, 4)
    
    match user_input:
        case 0: 
            os.system("clear")
            print("Gracias por usar el programa! Nos vemos pronto! ")
            break
        case 1: 
            participantes = registrar_participantes(participantes)
            matriz_puntuación = definir_matriz(matriz_puntuacion, participantes, cant_jurados)
            
        case 2:
            os.system("clear")
            print("--- Menu de Carga de Puntuaciones --- \n\n -> (1) Ver lista de Participantes\n -> (2) Buscar participantes por nombre\n -> (0) Volver al menú anterior")
            user_input = pedir_dato(" Elegí una opción para proceder: ", int, 0, 2)

            match user_input:
                case 1: 
                    os.system("clear")
                    print("-> Lista de Participantes: \n")
                    for i in range(len(participantes)):
                        print(i+1, participantes[i])
                    participante_input = pedir_dato("\nIngrese el número de participante a cargar la puntuación: ", int, 1, len(participantes)                        )
                    os.system("clear")
                    carga_puntuacion(matriz_puntuacion, participantes, participante_input-1, cant_jurados)
                
                case 2: 
                    os.system("clear")
                    user_input = pedir_dato(" Ingrese el nombre del participante a buscar: ", str, 3) 
                    encontrado = False
                    for i in range(len(participantes)):
                        if participantes[i].lower() == user_input.lower():
                            print(f"Participante {participantes[i]} encontrado! Procediendo a la carga de puntuación: ")
                            carga_puntuacion(matriz_puntuacion, participantes, i, cant_jurados)
                            encontrado = True
                            break
                    if not encontrado:
                        print("Participante no encontrado. Intentalo de nuevo.")
                    
        case 3: 
            os.system("clear")
            print("-> (0) Buscar participante por nombre\n -> (1) Mostrar puntuaciones por participante\n -> (2) Mostrar participantes con promedio mayor a 4\n -> (3) Mostrar participantes con promedio mayor a 7\n -> (4) Mostrar promedio de cada jurado\n -> (5) Mostrar jurado más estricto\n -> (6) Mostrar Top 3 de Participantes \n -> (7) Mostrar todos los participantes \n -> (0) Volver al menú anterior. \n\n")
            user_input = pedir_dato(" Elegí una opción para proceder: ", int, 0, 7)
            
            match user_input:
                case 0:
                    os.system("clear")
                    print("Gracias por usar el programa! Nos vemos pronto! ")
                    break
                    # case 1: 
                    # case 2: 
                    # case 3:
                    # case 4:
                    # case 5: 
                    # case 6:
                    # case 7: 
        case 4:
            os.system("clear")
            cant_jurados = pedir_dato("\nIngresa la nueva cantidad de jurados: ", int, 0)
            matriz_puntuación = definir_matriz(matriz_puntuacion, participantes, cant_jurados)
