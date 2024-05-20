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

nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))
print(f"\n¡Hola, {nombre}! Bienvenido al cuestionario. \nPor favor contesta con honestidad :)")

# Generar la lista de posiciones hasta p16
lista_posiciones = [f'P{i}' for i in range(1, 15)]

preguntas = [
    "\n1. ¿Cuál es el objetivo fundamental de su inversión? \nA) Invertir en valores que son fácilmente convertibles en efectivo (Liquidez) \nB) Tratar de generar una renta periódica de la inversión en forma de intereses o dividendos (Ingreso) \nC) El objetivo de las inversiones es lograr un crecimiento a largo plazo del capital a través de la reinversión de los rendimientos en el principal (Crecimiento) \nD) Se busca realizar inversiones con el objetivo de obtener mayores rentabilidades a cambio de mayores niveles a la exposición al riesgo (Especulativo)",
    "\n2. ¿En qué rango de edad se encuentra? \nA) Menor de 25 años \nB) Entre 25-40 años \nC) Entre 40-60 años \nD) Más de 60 años",
    "\n3. ¿Ha tenido experiencia invirtiendo? \nA) Si \nB) No",
    "\n4. En términos de tiempo, ¿cuál es su horizonte de inversión? \nA) Menos de 1 año \nB) Entre 1 y 3 años \nC) Más de 3 años",
    "\n5. ¿Conoce alguna de las siguientes opciones de inversión? \nA) Opciones de inversión en el mercado nacional \nB) Opciones de inversión en el mercado internacional \nC) No conozco ninguna",
    "\n6. ¿Utiliza medios propios para evaluar y dar seguimiento a instrumentos financieros y a mercados bursátiles? \nA) Si \nB) No",
    "\n7. A la hora de tomar una decisión de inversión, ¿cuál de los siguientes factores incide más sobre ésta? \nA) Análisis elaborados personalmente sobre el instrumento financiero \nB) Información técnica suministrada por su Casa de Bolsa \nC) El criterio de su asesor \nD) Experiencias anteriores \nE) Otras",
    "\n8. En el caso de altas fluctuaciones de precios de sus inversiones en un periodo determinado, las cuales lo exponen a pérdidas de capital, ¿qué decisión tomaría? \nA) No me siento cómodo con las fluctuaciones \nB) Liquidar inmediatamente las posiciones ante tales fluctuaciones \nC) Esperaría un tiempo prudente para analizar la tendencia del mercado \nD) Mantendría las posiciones esperando una recuperación en el mediano o largo plazo",
    "\n9.- Si el valor de sus inversiones cae ¿A partir de qué monto tomaría medidas extremas? Opciones para pregunta 9: \nA) -5% \nB) -10% \nC) -20% \nD) No me inquieto",
    "\n10.- ¿Cuál de las siguientes afirmaciones se ajusta más a sus preferencias? Opciones para pregunta 10: \nA) Mis inversiones deben ser lo más seguras posibles, aunque eso implique que los rendimientos sean más bajos \nB) Me interesan rendimientos más competitivos manteniendo una adecuada seguridad, pero sabiendo que estoy expuesto a riesgos de pérdidas ocasionales \nC) Busco rendimientos superiores a los del mercado y estoy dispuesto a aceptar un riesgo moderado para obtener estos rendimientos \nD) Espero altos rendimientos en el largo plazo, aunque ello signifique aceptar fluctuaciones en los resultados de corto plazo y asumir mayores niveles de riesgo",
    "\n11.- Defina su moneda de preferencia para realizar inversiones (puede marcar más de una opción) Opciones para pregunta 11: \nA) Pesos \nB) Dolares \nC) Euros \nD) Otra: \nE) No tengo preferencias por una moneda en particular",
    "\n12.- De acuerdo a la definición anterior ¿se considera un inversionista sofisticado? Opciones para pregunta 12: \nA) Si \nB) No",
    "\n13.- ¿Cuenta con portafolio de inversión en otras instituciones financieras? Opciones para pregunta 13: \nA) Si \nB) No",
    "\n14.- ¿Cuenta con inversiones de naturaleza no financiera (negocios, bienes raices, etc.)? Opciones para pregunta 14: \nA) Si, en: \n   * Tecnología (Software, equipo) \n   * Inversión agrícola (semillas, cultivo, maquinaria, etc.) \n   * Inversión en comercio \n   * Inversión en infraestructura \n   * Inversión inmobiliaria \n   * Otras: \nB) No"
]
preguntas_dict = {
    "1. ¿Cuál es el objetivo fundamental de su inversión?": {
        "A": "Invertir en valores que son fácilmente convertibles en efectivo (Liquidez)",
        "B": "Tratar de generar una renta periódica de la inversión en forma de intereses o dividendos (Ingreso)",
        "C": "El objetivo de las inversiones es lograr un crecimiento a largo plazo del capital a través de la reinversión de los rendimientos en el principal (Crecimiento)",
        "D": "Se busca realizar inversiones con el objetivo de obtener mayores rentabilidades a cambio de mayores niveles a la exposición al riesgo (Especulativo)"
    },
    "2. ¿En qué rango de edad se encuentra?": {
        "A": "Menor de 25 años",
        "B": "Entre 25-40 años",
        "C": "Entre 40-60 años",
        "D": "Más de 60 años"
    },
    "3. ¿Ha tenido experiencia invirtiendo?": {
        "A": "Si",
        "B": "No"
    },
    "4. En términos de tiempo, ¿cuál es su horizonte de inversión?": {
        "A": "Menos de 1 año",
        "B": "Entre 1 y 3 años",
        "C": "Más de 3 años"
    },
    "5. ¿Conoce alguna de las siguientes opciones de inversión?": {
        "A": "Opciones de inversión en el mercado nacional",
        "B": "Opciones de inversión en el mercado internacional",
        "C": "No conozco ninguna"
    },
    "6. ¿Utiliza medios propios para evaluar y dar seguimiento a instrumentos financieros y a mercados bursátiles?": {
        "A": "Si",
        "B": "No"
    },
    "7. A la hora de tomar una decisión de inversión, ¿cuál de los siguientes factores incide más sobre ésta?": {
        "A": "Análisis elaborados personalmente sobre el instrumento financiero",
        "B": "Información técnica suministrada por su Casa de Bolsa",
        "C": "El criterio de su asesor",
        "D": "Experiencias anteriores",
        "E": "Otras"
    },
    "8. En el caso de altas fluctuaciones de precios de sus inversiones en un periodo determinado, las cuales lo exponen a pérdidas de capital, ¿qué decisión tomaría?": {
        "A": "No me siento cómodo con las fluctuaciones",
        "B": "Liquidar inmediatamente las posiciones ante tales fluctuaciones",
        "C": "Esperaría un tiempo prudente para analizar la tendencia del mercado",
        "D": "Mantendría las posiciones esperando una recuperación en el mediano o largo plazo"
    },
    "9.- Si el valor de sus inversiones cae ¿A partir de qué monto tomaría medidas extremas?": {
        "A": "-5%",
        "B": "-10%",
        "C": "-20%",
        "D": "No me inquieto"
    },
    "10.- ¿Cuál de las siguientes afirmaciones se ajusta más a sus preferencias?": {
        "A": "Mis inversiones deben ser lo más seguras posibles, aunque eso implique que los rendimientos sean más bajos",
        "B": "Me interesan rendimientos más competitivos manteniendo una adecuada seguridad, pero sabiendo que estoy expuesto a riesgos de pérdidas ocasionales",
        "C": "Busco rendimientos superiores a los del mercado y estoy dispuesto a aceptar un riesgo moderado para obtener estos rendimientos",
        "D": "Espero altos rendimientos en el largo plazo, aunque ello signifique aceptar fluctuaciones en los resultados de corto plazo y asumir mayores niveles de riesgo"
    },
    "11.- Defina su moneda de preferencia para realizar inversiones (puede marcar más de una opción)": {
        "A": "Pesos",
        "B": "Dolares",
        "C": "Euros",
        "D": "Otra:",
        "E": "No tengo preferencias por una moneda en particular"
    },
    "12.- De acuerdo a la definición anterior ¿se considera un inversionista sofisticado?": {
        "A": "Si",
        "B": "No"
    },
    "13.- ¿Cuenta con portafolio de inversión en otras instituciones financieras?": {
        "A": "Si",
        "B": "No"
    },
    "14.- ¿Cuenta con inversiones de naturaleza no financiera (negocios, bienes raices, etc.)?": {
        "A": "Si, en:",
        "B": "No"
    }
}
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

for pregunta in preguntas:
    print(pregunta)

    respuesta = str(input("Ingrese la letra correspondiente a su respuesta: ")).strip().upper()

    if respuesta not in ["A", "B", "C", "D"]:
        print("Opción inválida.")
    else:
        respuestas.append(respuesta)
        
i = calcular_puntos(respuestas)
print("-------------------------------------------------------\nPuntos obtenidos:", i) 

def asignar_perfil(valor):
    if respuesta_pregunta_12 == 'A':
        return "Sofisticado: Busca una elevada rentabilidad tomando posiciones de mayor riesgo. Es conocedor del mercado y los riesgos inherentes al mismo. Se hace responsable de sus propias inversiones."
    elif valor <= 14:
        return "Adverso al riesgo: Prefiere una menor exposición al riesgo, esto podrá significar una menor rentabilidad y una mayor probabilidad de preservar el capital"
    elif valor <= 28:
        return "Moderado: Está dispuesto a invertir parte de su capital en títulos con cierta exposición al riesgo, esperando una mayor rentabilidad."
    elif valor <= 64:
        return "Propenso al Riesgo: Asume una fuerte exposición al riesgo, apostando a tener una elevada rentabilidad."
    else:
        return "Fuera de Rango"


respuesta_pregunta_12 = respuestas[11] if len(respuestas) > 11 else ''
perfil = asignar_perfil(i)

print("Perfil asignado:\n", perfil)

perfil_propuesto = ""

satisfaccion_perfil = input("\n15.-¿Está usted de acuerdo con el perfil asignado? (Selecciona la letra correspondiente)\nA) Sí\nB) No\nRespuesta: ").strip().lower()

if satisfaccion_perfil == "b":

    print("\n16.-¿Cuál considera que es el perfil correcto para usted?")
    print("A) Adverso al riesgo")
    print("B) Moderado")
    print("C) Propenso al Riesgo")
    print("D) Sofisticado")
    perfil_propuesto_respuesta = input("Respuesta: ").strip().upper()
    if perfil_propuesto_respuesta == "A":
        perfil_propuesto = "Adverso al riesgo"
    elif perfil_propuesto_respuesta == "B":
        perfil_propuesto = "Moderado"
    elif perfil_propuesto_respuesta == "C":
        perfil_propuesto = "Propenso al Riesgo"
    elif perfil_propuesto_respuesta == "D":
        perfil_propuesto = "Sofisticado"
    else:
        print("Respuesta no válida.")
    print("Perfil propuesto:", perfil_propuesto)
    
print("\n--- Resumen de respuestas ---")
print("Fecha y hora de realización:", fecha_actual) 
print("Nombre:", nombre)
print("Edad:", edad)
print("Perfil asignado:", perfil)
if perfil_propuesto:
    print("Perfil propuesto:", perfil_propuesto)
