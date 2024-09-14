# %% [markdown]
# ### Paso 4. Análisis exploratorio de datos (Python)

# %% [markdown]
# Además de los datos que recuperaste en las tareas anteriores te han dado un segundo archivo. Ahora tienes estos dos CSV:
# 
# project_sql_result_01.csv. Contiene los siguientes datos:
# - company_name: nombre de la empresa de taxis
# - trips_amount: el número de viajes de cada compañía de taxis el 15 y 16 de noviembre de 2017.
# 
# project_sql_result_04.csv. Contiene los siguientes datos:
# - dropoff_location_name: barrios de Chicago donde finalizaron los viajes
# - average_trips: el promedio de viajes que terminaron en cada barrio en noviembre de 2017.
# 
# Para estos dos datasets ahora necesitas:
# 
# - importar los archivos
# - estudiar los datos que contienen
# - asegurarte de que los tipos de datos sean correctos
# - identificar los 10 principales barrios en términos de finalización
# - hacer gráficos: empresas de taxis y número de viajes, los 10 barrios principales por número de finalizaciones
# - sacar conclusiones basadas en cada gráfico y explicar los resultados

# %%
# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as st

# %%
# Importar Archivos para los dataframes
df1= pd.read_csv("../datasets/project_sql_result_01.csv")
df2 = pd.read_csv("../datasets/project_sql_result_04.csv")
df3 = pd.read_csv("../datasets/project_sql_result_07.csv")

# %%
# Estudiar los datos contenidos en los dataframe y verificar los tipos de datos

# Primer dataframe
print(('===== Datos de compañias ====='))
print(df1.head())
print(df1.info())
print(('--------------------------------'))

# Segundo Dataframe
print(('===== Datos de finalizacion de los viajes ====='))
print(df2.head())
print(df2.info())
print(('--------------------------------'))

# Tercer dataframe
print(('===== Datos de condiciones climaticas de los viajes ====='))
print(df3.head(10))
print(df3.info())

# %%
# Identificar los 10 barrios principales en termino de finalizacion
top_10_dropoff = df2.sort_values(by = 'average_trips' ,ascending=False).head(10)
print(('==== Los principales 10 barrios en terminos de finalizacion del recorrido ===='))
print(top_10_dropoff)

# %%
# Grafico Empresas de taxi y numero de viajes
top_10_taxi_company = df1.head(10)

plt.figure(figsize=(12,6))
plt.bar(top_10_taxi_company['company_name'], top_10_taxi_company['trips_amount'])
plt.xticks(rotation=90)
plt.xlabel('Empresa de taxis')
plt.ylabel('Numero de viajes')
plt.title('Numero de viajes por empresa de Taxis')
plt.show()


# %% [markdown]
# #### Conclusion grafico de Numero de viajes por empresa de Taxis

# %% [markdown]
# En este grafico se representa la cantidad de viajes realizados para las 10 principales compañias, las compañias que presentan mas cantidad de viaje.
# 
# A continuacion las barras indican en orden descendente las compañias con mas viajes comenzando por Flash cab.
# 
# Flash cab figura como la compañia que mas viajes realiza destacandose del resto de las compañias por su gran volumen de viajes a comparacion del resto de compañias, podemos notar como el resto de las compañias se presenta una disminucion progresiva en la cantidad de viajes realizados pero sin tanta diferencia como lo es del top 1 al 2.
# 
# Hablando de cifras exactas estamos hablando que Flash cab posee 19558 viajes realizados en el top 1 mientras que el top 2 Taxi Affiliation Services muestra 11422 viajes, dejando una diferencia de 8136 viajes; Mientras que del top 2 al top 3(Medallion Leasin con 10367 viajes) hay una diferencia de 1055 viajes.

# %%
# Top 10 Barrios por Promedio de Finalizaciones de Viaje
plt.figure(figsize=(12,6))
plt.bar(top_10_dropoff['dropoff_location_name'], top_10_dropoff['average_trips'])
plt.xticks(rotation=90)
plt.xlabel('Barrio de Finalización del Viaje')
plt.ylabel('Promedio de Viajes')
plt.title('Top 10 Barrios por Promedio de Finalizaciones de Viaje')
plt.show()


# %% [markdown]
# #### Conclusion de grafico de Top 10 Barrios por Promedio de Finalizaciones de Viaje

# %% [markdown]
# En este grafico de barras representa un top 10 de los barrios que son mas frecuentados por las compañias de taxi.
# 
# Se puede observar que el barrio mas visitado es el barrio "Loop" seguido de "River North" y "Streeterville"; mientras que los barrios "Gold Coast" y "Sheffield & DePaul" son los menos visitados de estos 10 barrios.
# 
# Podemos observar que el barrio Loop es el mas frecuentado de los 10 barrios mostrados en la grafica, un promedio elevado sugiere que esta es una zona o area clave en terminos de activiadad economica, turimso o densidad de poblacion. Para las compañias de taxi estos barrios podrian ser areas prioritarias y con base a ello desempeñar medidas para mejorar su servicio en estas zonas.

# %% [markdown]
# ### Paso 5. Prueba de hipótesis (Python)

# %% [markdown]
# #### Hipotesis: "La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos"

# %% [markdown]
# Para probar la hipotesis vamos a plantear primeros las hipotesis nula (H0) y la alternativa (H1) tambien para este caro vamos a establecer el valor de alpha en 0.05 lo cual significa que estmos dispuestos a aceptar un 5% de probabilidad de rechazar la hipotesis nula cuando en realidad es verdadera (Error de tipo 1)
# 
# Hipotesis nula (H0): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare NO cambia los sábados lluviosos.
# 
# Hipotesis Alternativa (H1): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos
# 
# Alpha = 0.05

# %%
# Filtramos datos para las condiciones buenas y malas del clima
good_weather = df3[df3['weather_conditions'] == 'Good']['duration_seconds']
bad_weather = df3[df3['weather_conditions'] == 'Bad']['duration_seconds']


# Establecemos valor alpha
alpha = 0.05

# Realizamos la prueba t para los generos Action y Sports
results = st.ttest_ind(good_weather, bad_weather)

# Mostramos el Valor de P
print('valor p:', results.pvalue)  

# Si p es menos que alpha podemos rechazar la hipotesis nula 
if (results.pvalue < alpha):
    print("Aprobamos Hipotesis Alternativa")
    print("Hipotesis Alternativa (H1): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos")
else:
    print("Aprobamos la Hipotesis Nula")
    print("Hipotesis nula (H0): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare NO cambia los sábados lluviosos.")



