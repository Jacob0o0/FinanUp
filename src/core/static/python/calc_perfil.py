import datetime
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

puntos_por_inciso = {
    'P1' : {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4
    },
    'P2' : {
        'A' : 4,
        'B' : 3,
        'C' : 2,
        'D' : 1
    },
    'P3' : {
        'A' : 2,
        'B' : 1
    },
    'P4' : {
        'A' : 1,
        'B' : 2,
        'C' : 3
    },
    'P5' : {
        'A' : 2,
        'B' : 3,
        'C' : 1,
        'D' : 3
    },
    'P6' : {
        'A' : 2,
        'B' : 1
    },
    'P7' : {
        'A' : 2,
        'B' : 1,
        'C' : 3,
        'D' : 4
    },
    'P8' : {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4
    },
    'P9' : {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4
    },
    'P10' : {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4
    },
    'P11' : {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4
    },
    'P12' : {
        'A' : 2,
        'B' : 1
    },
    'P13' : {
        'A' : 2,
        'B' : 1
    },
    'P14' : {
        'A' : 2,
        'B' : 1
    }
}

# Generar la lista de posiciones hasta p16
lista_posiciones = [f'P{i}' for i in range(1, 15)]

respuestas = []

def calcular_puntos(respuestas_usuario):
    total_puntos = 0
    i = 0
    for respuesta in respuestas_usuario:
        if respuesta in puntos_por_inciso[lista_posiciones[i]]:
            pregunta = puntos_por_inciso[lista_posiciones[i]]
            total_puntos += pregunta[respuesta]
        i += 1
    return total_puntos

def asignar_perfil(respuestas, valor):
    if respuestas[11] == 'A':
        return "Sofisticado"
    elif valor <= 14:
        return "Adverso al riesgo"
    elif valor <= 28:
        return "Moderado"
    elif valor <= 64:
        return "Propenso al Riesgo"
    else:
        return "Fuera de Rango"

if __name__ == "__main__":
    calcular_puntos()