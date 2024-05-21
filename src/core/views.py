from django.shortcuts import render
from django import forms
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {}

    preguntas_dictL = {
        "¿Cuál es el objetivo fundamental de su inversión?": {
            "A": "Invertir en valores que son fácilmente convertibles en efectivo (Liquidez)",
            "B": "Tratar de generar una renta periódica de la inversión en forma de intereses o dividendos (Ingreso)",
            "C": "El objetivo de las inversiones es lograr un crecimiento a largo plazo del capital a través de la reinversión de los rendimientos en el principal (Crecimiento)",
            "D": "Se busca realizar inversiones con el objetivo de obtener mayores rentabilidades a cambio de mayores niveles a la exposición al riesgo (Especulativo)"
        },
        "¿En qué rango de edad se encuentra?": {
            "A": "Menor de 25 años",
            "B": "Entre 25-40 años",
            "C": "Entre 40-60 años",
            "D": "Más de 60 años"
        },
        "¿Ha tenido experiencia invirtiendo?": {
            "A": "Si",
            "B": "No"
        },
        "En términos de tiempo, ¿cuál es su horizonte de inversión?": {
            "A": "Menos de 1 año",
            "B": "Entre 1 y 3 años",
            "C": "Más de 3 años"
        },
        "¿Conoce alguna de las siguientes opciones de inversión?": {
            "A": "Opciones de inversión en el mercado nacional",
            "B": "Opciones de inversión en el mercado internacional",
            "C": "No conozco ninguna"
        },
        "¿Utiliza medios propios para evaluar y dar seguimiento a instrumentos financieros y a mercados bursátiles?": {
            "A": "Si",
            "B": "No"
        },
        "A la hora de tomar una decisión de inversión, ¿cuál de los siguientes factores incide más sobre ésta?": {
            "A": "Análisis elaborados personalmente sobre el instrumento financiero",
            "B": "Información técnica suministrada por su Casa de Bolsa",
            "C": "El criterio de su asesor",
            "D": "Experiencias anteriores",
            "E": "Otras"
        }
    }
    preguntas_dictR = {
        "En el caso de altas fluctuaciones de precios de sus inversiones en un periodo determinado, las cuales lo exponen a pérdidas de capital, ¿qué decisión tomaría?": {
            "A": "No me siento cómodo con las fluctuaciones",
            "B": "Liquidar inmediatamente las posiciones ante tales fluctuaciones",
            "C": "Esperaría un tiempo prudente para analizar la tendencia del mercado",
            "D": "Mantendría las posiciones esperando una recuperación en el mediano o largo plazo"
        },
        "Si el valor de sus inversiones cae ¿A partir de qué monto tomaría medidas extremas?": {
            "A": "-5%",
            "B": "-10%",
            "C": "-20%",
            "D": "No me inquieto"
        },
        "¿Cuál de las siguientes afirmaciones se ajusta más a sus preferencias?": {
            "A": "Mis inversiones deben ser lo más seguras posibles, aunque eso implique que los rendimientos sean más bajos",
            "B": "Me interesan rendimientos más competitivos manteniendo una adecuada seguridad, pero sabiendo que estoy expuesto a riesgos de pérdidas ocasionales",
            "C": "Busco rendimientos superiores a los del mercado y estoy dispuesto a aceptar un riesgo moderado para obtener estos rendimientos",
            "D": "Espero altos rendimientos en el largo plazo, aunque ello signifique aceptar fluctuaciones en los resultados de corto plazo y asumir mayores niveles de riesgo"
        },
        "Defina su moneda de preferencia para realizar inversiones (puede marcar más de una opción)": {
            "A": "Pesos",
            "B": "Dolares",
            "C": "Euros",
            "D": "Otra:",
            "E": "No tengo preferencias por una moneda en particular"
        },
        "De acuerdo a la definición anterior ¿se considera un inversionista sofisticado?": {
            "A": "Si",
            "B": "No"
        },
        "¿Cuenta con portafolio de inversión en otras instituciones financieras?": {
            "A": "Si",
            "B": "No"
        },
        "¿Cuenta con inversiones de naturaleza no financiera (negocios, bienes raices, etc.)?": {
            "A": "Si, en:",
            "B": "No"
        }
    }

    context['preguntas_dictL'] = preguntas_dictL
    context['preguntas_dictR'] = preguntas_dictR

    return render(request, 'home.html', context=context)
    
def investor_view(request):

    context = {}

    preguntas_dictL = {
        "¿Cuál es el objetivo fundamental de su inversión?": {
            "A": "Invertir en valores que son fácilmente convertibles en efectivo (Liquidez)",
            "B": "Tratar de generar una renta periódica de la inversión en forma de intereses o dividendos (Ingreso)",
            "C": "El objetivo de las inversiones es lograr un crecimiento a largo plazo del capital a través de la reinversión de los rendimientos en el principal (Crecimiento)",
            "D": "Se busca realizar inversiones con el objetivo de obtener mayores rentabilidades a cambio de mayores niveles a la exposición al riesgo (Especulativo)"
        },
        "¿En qué rango de edad se encuentra?": {
            "A": "Menor de 25 años",
            "B": "Entre 25-40 años",
            "C": "Entre 40-60 años",
            "D": "Más de 60 años"
        },
        "¿Ha tenido experiencia invirtiendo?": {
            "A": "Si",
            "B": "No"
        },
        "En términos de tiempo, ¿cuál es su horizonte de inversión?": {
            "A": "Menos de 1 año",
            "B": "Entre 1 y 3 años",
            "C": "Más de 3 años"
        },
        "¿Conoce alguna de las siguientes opciones de inversión?": {
            "A": "Opciones de inversión en el mercado nacional",
            "B": "Opciones de inversión en el mercado internacional",
            "C": "No conozco ninguna"
        },
        "¿Utiliza medios propios para evaluar y dar seguimiento a instrumentos financieros y a mercados bursátiles?": {
            "A": "Si",
            "B": "No"
        },
        "A la hora de tomar una decisión de inversión, ¿cuál de los siguientes factores incide más sobre ésta?": {
            "A": "Análisis elaborados personalmente sobre el instrumento financiero",
            "B": "Información técnica suministrada por su Casa de Bolsa",
            "C": "El criterio de su asesor",
            "D": "Experiencias anteriores",
            "E": "Otras"
        }
    }
    preguntas_dictR = {
        "En el caso de altas fluctuaciones de precios de sus inversiones en un periodo determinado, las cuales lo exponen a pérdidas de capital, ¿qué decisión tomaría?": {
            "A": "No me siento cómodo con las fluctuaciones",
            "B": "Liquidar inmediatamente las posiciones ante tales fluctuaciones",
            "C": "Esperaría un tiempo prudente para analizar la tendencia del mercado",
            "D": "Mantendría las posiciones esperando una recuperación en el mediano o largo plazo"
        },
        "Si el valor de sus inversiones cae ¿A partir de qué monto tomaría medidas extremas?": {
            "A": "-5%",
            "B": "-10%",
            "C": "-20%",
            "D": "No me inquieto"
        },
        "¿Cuál de las siguientes afirmaciones se ajusta más a sus preferencias?": {
            "A": "Mis inversiones deben ser lo más seguras posibles, aunque eso implique que los rendimientos sean más bajos",
            "B": "Me interesan rendimientos más competitivos manteniendo una adecuada seguridad, pero sabiendo que estoy expuesto a riesgos de pérdidas ocasionales",
            "C": "Busco rendimientos superiores a los del mercado y estoy dispuesto a aceptar un riesgo moderado para obtener estos rendimientos",
            "D": "Espero altos rendimientos en el largo plazo, aunque ello signifique aceptar fluctuaciones en los resultados de corto plazo y asumir mayores niveles de riesgo"
        },
        "Defina su moneda de preferencia para realizar inversiones (puede marcar más de una opción)": {
            "A": "Pesos",
            "B": "Dolares",
            "C": "Euros",
            "D": "Otra:",
            "E": "No tengo preferencias por una moneda en particular"
        },
        "De acuerdo a la definición anterior ¿se considera un inversionista sofisticado?": {
            "A": "Si",
            "B": "No"
        },
        "¿Cuenta con portafolio de inversión en otras instituciones financieras?": {
            "A": "Si",
            "B": "No"
        },
        "¿Cuenta con inversiones de naturaleza no financiera (negocios, bienes raices, etc.)?": {
            "A": "Si, en:",
            "B": "No"
        }
    }

    context['preguntas_dictL'] = preguntas_dictL
    context['preguntas_dictR'] = preguntas_dictR

    if request.method == 'POST':
        data = request.POST
        resultados = {}
        for key in data:
            if key.startswith('pregunta'):
                resultados[key] = data[key]
        # Puedes hacer lo que necesites con los datos aquí
        # Por ejemplo, guardar en la base de datos, analizar los datos, etc.
        context['resultados'] = resultados

        context['type_investor'] = 'Moderado'

        return render(request, 'investor.html', context)
    else:
        return render(request, 'investor.html')