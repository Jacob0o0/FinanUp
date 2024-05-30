import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # Para mejorar la visualización con colores

from django.conf import settings
from scipy.optimize import minimize 

def obtener_datos(n_empresas):
    # Lista de nombres base de los archivos CSV correspondientes a las empresas
    csv_files = ['AAPL', 'AZN', 'DELL', 'DIS', 'IBM', 'INTC', 'META', 'MSFT', 'NVDA', 'SONY', 'PEP', 'WALMEX.MX', 'CEMEXCPO.MX', 'TLEVISACPO.MX', 'CHDRAUIB.MX', 'F']


    # Asegurarse de que n_empresas no exceda la cantidad de archivos disponibles
    n_empresas = min(n_empresas, len(csv_files))

    # Obtener los nombres de las primeras n_empresas
    nombres_empresas = csv_files[:n_empresas]

    # Construir la ruta completa para cada archivo CSV y leer los archivos
    dfs = []
    data_dir = os.path.join(settings.BASE_DIR, 'core', 'static', 'data')
    for nombre in nombres_empresas:
        csv_file_path = os.path.join(data_dir, f'{nombre}.csv')
        df = pd.read_csv(csv_file_path)
        dfs.append(df)
    
    #Utiliza max() para encontrar el DataFrame con la mayor cantidad de filas:
    df_mayor_filas = max(dfs, key=len)
    fechas_base = df_mayor_filas[['Date', 'Adj Close']]
    columnas_rendimiento = ['Rendimiento_' + nombre for nombre in nombres_empresas]
    df_nuevo = pd.DataFrame(columns=['Date'] + columnas_rendimiento)
    
    for index, fila in fechas_base.iterrows():
        fecha_base = fila['Date']

        # Crea una fila nueva para el DataFrame nuevo
        fila_nueva = {'Date': fecha_base}

        # Agrega los rendimientos para cada DataFrame
        for i, df in enumerate(dfs):
            if fecha_base in df['Date'].values:
                fila_nueva['Rendimiento_' + nombres_empresas[i]] = df[df['Date'] == fecha_base]['Adj Close'].values[0]
            else:
                fila_nueva['Rendimiento_' + nombres_empresas[i]] = np.nan

        df_nuevo = pd.concat([df_nuevo, pd.DataFrame([fila_nueva])], ignore_index=True)
    
    df_nuevo = df_nuevo.sort_values(by='Date')
    return df_nuevo, columnas_rendimiento

def calcular_nuevos_valores(df_nuevo, columnas_rendimiento, nombres_empresas):
    # Crear el DataFrame de rendimientos vacío
    df_rendimientos = pd.DataFrame(columns=['Date'] + columnas_rendimiento)

    # Primera fila (sin valores previos)
    primera_fila = df_nuevo.iloc[0].to_dict()
    fila_nueva_valores = {'Date': primera_fila['Date']}
    for i in range(len(columnas_rendimiento)):
        fila_nueva_valores['Rendimiento_' + nombres_empresas[i]] = 0  # Asignar 0 para el primer renglón
    df_rendimientos = pd.concat([df_rendimientos, pd.DataFrame([fila_nueva_valores])], ignore_index=True)

    # Restantes filas
    for index in range(1, len(df_nuevo)):
        fila_actual = df_nuevo.iloc[index]
        fecha_actual = fila_actual['Date']
        valores_rendimiento_actuales = fila_actual[columnas_rendimiento].tolist()

        fila_nueva_valores = {'Date': fecha_actual}
        fila_anterior = df_nuevo.iloc[index - 1][columnas_rendimiento].tolist()  # Valores de la fila anterior

        for i, valor_actual in enumerate(valores_rendimiento_actuales):
            divisor = fila_anterior[i] if fila_anterior[i] != 0 else 1
            nuevo_valor = (valor_actual - fila_anterior[i]) / divisor
            fila_nueva_valores['Rendimiento_' + nombres_empresas[i]] = nuevo_valor

        df_rendimientos = pd.concat([df_rendimientos, pd.DataFrame([fila_nueva_valores])], ignore_index=True)

    return df_rendimientos

def calcular_estadisticas_descriptivas(df):
    
    columnas_numericas = df.select_dtypes(include=['int64', 'float64'])  # Seleccionar columnas numéricas
    estadisticas = pd.DataFrame(columns=['Columna', 'Media', 'Varianza', 'Desviación Estándar'])

    for columna in columnas_numericas:
        estadisticas_columna = {
            'Columna': columna,
            'Media': df[columna].mean(),
            'Varianza': df[columna].var(),
            'Desviación Estándar': df[columna].std()
        }
        # Usar concat para agregar la fila a estadisticas
        estadisticas = pd.concat([estadisticas, pd.DataFrame([estadisticas_columna])], ignore_index=True)

    return estadisticas

def objetivo_min_riesgo(ponderaciones, matriz_covarianza):
    return np.sqrt(np.dot(ponderaciones.T, np.dot(matriz_covarianza, ponderaciones)))

# Maximizar el ratio de Sharpe
def objetivo_max_sharpe(ponderaciones, medias_rendimientos, matriz_covarianza):
    retorno_portafolio = np.dot(ponderaciones, medias_rendimientos)
    riesgo_portafolio = np.sqrt(np.dot(ponderaciones.T, np.dot(matriz_covarianza, ponderaciones)))
    return -retorno_portafolio / riesgo_portafolio

def plot_pie_chart(df_ponderaciones, title):
    labels = df_ponderaciones['Empresa']
    sizes = df_ponderaciones['Ponderacion_Optima']
    explode = [0.1] * len(labels)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.set_title(title)

def plot_resultados():
    plt.show()

def generarPDF(num_empresas, capital):
    df_datos, columnas_rendimiento = obtener_datos(num_empresas)

    # Lista de nombres base de los archivos CSV correspondientes a las empresas
    csv_files = ['AAPL', 'AZN', 'DELL', 'DIS', 'IBM', 'INTC', 'META', 'MSFT', 'NVDA', 'SONY']
    # Asegurarse de que n_empresas no exceda la cantidad de archivos disponibles
    num_empresas = min(num_empresas, len(csv_files))

    # Obtener los nombres de las primeras n_empresas
    nombres_empresas = csv_files[:num_empresas]

    df_rendimientos = calcular_nuevos_valores(df_datos, columnas_rendimiento, nombres_empresas)
    
    # Tratamiento de datos
    df_rendimientos = df_rendimientos.fillna(0)
    df_rendimientos = pd.DataFrame(df_rendimientos)

    estadisticas_descriptivas = calcular_estadisticas_descriptivas(df_rendimientos)
    estadisticas = pd.DataFrame(estadisticas_descriptivas)

    # Filtrar solo las columnas de rendimiento (omitimos la columna 'Date')
    rendimientos = df_rendimientos[columnas_rendimiento]
    # Calcular la matriz de covarianza
    matriz_covarianza = rendimientos.cov()
    # Convertir la matriz de covarianza a un DataFrame
    df_matriz_covarianza = pd.DataFrame(matriz_covarianza)

    # Filtrar solo las columnas de rendimiento (omitimos la columna 'Date')
    rendimientos = df_rendimientos[columnas_rendimiento]
    # Calcular la matriz de correlación
    matriz_correlacion = rendimientos.corr()
    # Convertir la matriz de correlación a un DataFrame
    df_matriz_correlacion = pd.DataFrame(matriz_correlacion)

    # Calcular las ponderaciones
    ponderaciones = np.array([1/num_empresas] * num_empresas)

    matriz_markowitz = matriz_covarianza * np.outer(ponderaciones, ponderaciones)
    matriz_markowitz = pd.DataFrame(matriz_markowitz)
    
    medias_rendimientos = estadisticas_descriptivas['Media'].values

    # Verificar que las dimensiones coincidan
    if len(medias_rendimientos) != num_empresas:
        raise ValueError("El número de medias no coincide con el número de columnas de rendimiento.")
    
    retorno_portafolio = np.dot(ponderaciones, medias_rendimientos)
    varianza_portafolio = np.sum(matriz_markowitz.values)
    desviacion_portafolio = np.sqrt(varianza_portafolio)
    
    ratio_sharpe = retorno_portafolio/desviacion_portafolio

    valores = pd.DataFrame({
        'Retorno Portafolio': [retorno_portafolio],
        'Varianza Portafolio': [varianza_portafolio],
        'Desviacion Portafolio': [desviacion_portafolio],
        'Ratio_Sharpe': [ratio_sharpe]
    })

    # Restricciones
    constraints = ({'type': 'eq', 'fun': lambda ponderaciones: np.sum(ponderaciones) - 1})
    bounds = tuple((0, 1) for _ in range(num_empresas))

    def objetivo_min_riesgo(ponderaciones):
        return np.sqrt(np.dot(ponderaciones.T, np.dot(matriz_covarianza, ponderaciones)))

    # Optimización
    resultado_min = minimize(objetivo_min_riesgo, ponderaciones, method='SLSQP', bounds=bounds, constraints=constraints)
    ponderaciones_optimasMin = resultado_min.x

    df_ponderacionesMin = pd.DataFrame({
        'Empresa': columnas_rendimiento,
        'Ponderacion_Optima': np.round(ponderaciones_optimasMin,4),
        'Resultado_Capital': np.round(ponderaciones_optimasMin * capital,2),
        'Porcentaje': np.round(ponderaciones_optimasMin * 100, 4) 
    })


    # Maximizar el ratio de Sharpe
    def objetivo_max_sharpe(ponderaciones):
        retorno_portafolio = np.dot(ponderaciones, medias_rendimientos)
        riesgo_portafolio = np.sqrt(np.dot(ponderaciones.T, np.dot(matriz_covarianza, ponderaciones)))
        return -retorno_portafolio / riesgo_portafolio
    
    # Optimización
    resultado_max = minimize(objetivo_max_sharpe, ponderaciones, method='SLSQP', bounds=bounds, constraints=constraints)
    ponderaciones_optimasMax = resultado_max.x

    df_ponderacionesMax = pd.DataFrame({
        'Empresa': columnas_rendimiento,
        'Ponderacion_Optima': np.round(ponderaciones_optimasMax,4),
        'Resultado_Capital': np.round(ponderaciones_optimasMax * capital,2),
        'Porcentaje': np.round(ponderaciones_optimasMax * 100, 4)
    })

    data_dir = os.path.join(settings.BASE_DIR, 'core', 'static', 'imgs')

    # Crear una figura con subplots
    fig, axs = plt.subplots(2, 3, figsize=(15, 15))

    # Graficar los datos en cada subplot
    plot_pie_chart(df_ponderacionesMin, 'Ponderaciones Óptimas por Empresa (Minimización de Riesgo)')
    plot_pie_chart(df_ponderacionesMax, 'Ponderaciones Óptimas por Empresa (Maximización del Sharpe Ratio)')
    
    df_rendimientos.plot(ax=axs[0, 0], title='Rendimientos')  # Suponiendo que estadisticas es un DataFrame con datos para graficar
    estadisticas.plot.bar(ax=axs[0, 1], title='Estadisticas Descriptivas')  # Suponiendo que df_matriz_covarianza es un DataFrame con datos para graficar
    # Crear un subplot específico para la matriz de covarianza
    axs[0, 2].imshow(df_matriz_covarianza, cmap='coolwarm', aspect='auto')
    axs[0, 2].set_title('Matriz de Covarianza') # Suponiendo que df_matriz_correlacion es un DataFrame con datos para graficar

    axs[1, 0].imshow(df_matriz_correlacion, cmap='coolwarm', aspect='auto')
    axs[1, 0].set_title('Matriz de Correlación') # Suponiendo que df_matriz_correlacion es un DataFrame con datos para graficar
    axs[1, 1].imshow(matriz_markowitz, cmap='coolwarm', aspect='auto')
    axs[1, 1].set_title('Matriz de Markowitz') # Suponiendo que df_matriz_correlacion es un DataFrame con datos para graficar

    # Ajustar el espaciado entre los subplots
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

