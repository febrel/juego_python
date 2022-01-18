from flask import Flask
import random

bandera_interna = True

def juego_base(respuesta):
    
    # Listas utilizadas
    base_juego = ['Piedra', 'Papel', 'Tijeras']
    resultados = []

    # Variables  generadas
    valor = random.randint(0, 2)
    bandera = 1
    cadena = ''

    # Comparar si existe una opción ganadora
    if (base_juego[respuesta] == 'Piedra' and base_juego[valor] == 'Papel'):
        bandera = 2
            
    elif (base_juego[respuesta] == 'Papel' and base_juego[valor] == 'Tijeras'):
        bandera = 2
            
    elif (base_juego[respuesta] == 'Tijeras' and base_juego[valor] == 'Piedra'):
        bandera = 2

    elif (base_juego[respuesta] == base_juego[valor] ):
        bandera = 3



    # Condicional que verifica el resultado final
    if (bandera == 1):
        cadena = 'Ganaste!'

    elif (bandera == 2):
        cadena = 'Perdiste!'
        
    elif (bandera == 3):
        cadena = 'Empataste!'

    # Guarda en la lista (resultado, respuesta_tuya, respuesta_contricante)
    resultados = [cadena, base_juego[respuesta], base_juego[valor] ]
    
    return resultados