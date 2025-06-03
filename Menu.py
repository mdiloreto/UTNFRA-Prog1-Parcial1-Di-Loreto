import os
from Funciones import *

cant_jurados = 3
participantes = [] 
matriz_puntuacion = init_matriz()

# Opcional para PRUEBAS
matriz_puntuacion, participantes = cargar_datos_ejemplo(matriz_puntuacion, participantes, cant_jurados)

while True: 
    os.system("clear")
    print("¡COMPETENCIA ABIERTA DE ACADEMIA DE BAILE! ")
    print(" --- MENU DE OPCIONES: ---\n\n -> (1) Registrar participantes \n -> (2) Registrar puntuaciones del Jurado\n -> (3) Ver información de los Datos cargados\n -> (4) Definir la cantidad de jurados \n -> (0) Salir del programa. \n")
    
    # Opcional para PRUEBAS
    print("Lista de Participantes", participantes)
    print("Matriz de puntuaciones", matriz_puntuacion, "\n")

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
                    get_all_participantes(participantes)
                    participante_input = pedir_dato("\nIngrese el número de participante a cargar la puntuación o 0 para salir: ", int, 0, len(participantes))
                    if participante_input == 0:
                        os.system("clear")
                    else:
                        os.system("clear")
                        carga_puntuacion(matriz_puntuacion, participantes, participante_input-1, cant_jurados)
                        input("\nPresioná ENTER para volver al menú...")

                case 2: 
                    os.system("clear")
                    user_input = pedir_dato(" Ingrese el nombre del participante a buscar: ", str, 3) 
                    encontrado = buscar_participante(participantes, user_input)
                    if encontrado is None:
                        print("Usuario no encontrado!")
                    else:
                        carga_puntuacion(matriz_puntuacion, participantes, encontrado, cant_jurados)  
                          
        case 3: 
            while True: 
                os.system("clear")
                print(" -> (0) Buscar participante por nombre\n -> (1) Mostrar puntuaciones por participante\n -> (2) Mostrar participantes con promedio mayor a 4\n -> (3) Mostrar participantes con promedio mayor a 7\n -> (4) Mostrar promedio de cada jurado\n -> (5) Mostrar jurado más estricto\n -> (6) Mostrar Top 3 de Participantes \n -> (7) Mostrar todos los participantes \n -> (0) Volver al menú anterior. \n\n")
                user_input = pedir_dato(" Elegí una opción para proceder: ", int, 0, 7)
                
                match user_input:
                    #Opción para salir
                    case 0:
                        os.system("clear")
                        print("Gracias por usar el programa! Nos vemos pronto! ")
                        break
                    
                    # Mostrar puntuaciones 
                    case 1:
                        os.system("clear")
                        get_all_participantes(participantes)
                        participante_input = pedir_dato("\nIngrese el número de participante a mostrar la puntuación o 0 para volver al menú anterior: ", int, 0, len(participantes))
                        if participante_input == 0:
                            os.system("clear")
                        else: 
                            os.system("clear")
                            mostrar_puntuaciones(matriz_puntuacion, participantes, participante_input-1)
                            input("\nPresioná ENTER para volver al menú...")

                    # Promedio > 4
                    case 2:
                        os.system("clear")
                        promedios_4 = mostrar_promedio_mayor(matriz_puntuacion, participantes, 4)
                        print("Participantes con Promedio > a 4: ")
                        for idx in range(len(promedios_4)):
                            print(idx, promedios_4[idx])
                        input("\nPresioná ENTER para volver al menú...")
                        
                    # Promedio > 7
                    case 3:
                        os.system("clear")
                        promedios_7 = mostrar_promedio_mayor(matriz_puntuacion, participantes, 7)
                        print("Participantes con Promedio > a 7: ")
                        for idx in range(len(promedios_7)):
                            print(idx, promedios_7[idx])
                        input("\nPresioná ENTER para volver al menú...")
                        
                    # Promedio de cada jurado
                    case 4:
                        os.system("clear")
                        print("Promedio de cada jurado:\n")

                        proms = promedios_por_jurado(matriz_puntuacion)
                        if proms == []:
                            print("No hay puntuaciones cargadas.")
                        else:
                            for j in range(len(proms)):
                                print(f"Jurado {j+1}: {round(proms[j], 1)}")

                        input("\nENTER para volver al menú...")
                        
                    # jurado más estricto 
                    case 5:
                        os.system("clear")
                        print("Jurado/s más estricto/s:\n")

                        proms = promedios_por_jurado(matriz_puntuacion)
                        if proms == []:
                            print("No hay puntuaciones cargadas.")
                            input("\nENTER para volver...")
                            break
                        # 1) saco el promedio mínimo
                        prom_min = proms[0]
                        for p in proms:          
                            if p < prom_min:
                                prom_min = p
                                
                        # 2) recorro los promedios y agrego al jurado a la lista de jurado mas estricto
                        jurados_min = []
                        for j in range(len(proms)):
                            if proms[j] == prom_min:
                                jurados_min = jurados_min + [j]  
                                
                        # 3) muestro 1 o varios jurados mas estrictos 
                        for j in jurados_min:
                            print(f" -> Jurado {j+1} con promedio {prom_min}")

                        input("\nENTER para volver al menú...")            
                          
                    # Top 3 alumnos.       
                    # case 6:
                    # Mostrar participantes ordenados alfabeticamente. 
                    # case 7: 
        case 4:
            os.system("clear")
            cant_jurados = pedir_dato("\nIngresa la nueva cantidad de jurados: ", int, 0)
            matriz_puntuacion = definir_matriz(matriz_puntuacion, participantes, cant_jurados)
