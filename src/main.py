# main.py
from preprocessing.preprocessing import load_data, inspect_data, clean_data
from eda.eda import plot_top_10_taxi_company, plot_top_10_dropoff
from hypothesis_testing.hypothesis_testing import hypothesis_test
from utils.generate_report import save_report

# Cargar los datos
df1, df2, df3 = load_data()

# Inspeccionar datos
inspect_data(df1)
inspect_data(df2)
inspect_data(df3)

# Limpiar datos si es necesario
df1 = clean_data(df1)
df2 = clean_data(df2)
df3 = clean_data(df3)

# Análisis exploratorio
plot_top_10_taxi_company(df1, 'taxi_company.png')
plot_top_10_dropoff(df2, 'dropoff_locations.png')

# Prueba de hipótesis
good_weather = df3[df3['weather_conditions'] == 'Good']['duration_seconds']
bad_weather = df3[df3['weather_conditions'] == 'Bad']['duration_seconds']
pvalue_hypothesis = hypothesis_test(good_weather, bad_weather)

# Contenido de reporte
report_content = """
<h1>Reporte Final de Analisis</h1>
<h2>Grafico: Numero de Viajes por Empresa de Taxis</h2>
<img src="images/taxi_company.png" alt="Grafico de Empresas de Taxis y Numero de Viajes">

<h2>Grafico: Top 10 Barrios por Promedio de Finalizacion de Viajes</h2>
<img src="images/dropoff_locations.png" alt="Grafico de Top 10 Barrios por Promedio de Finalizacion">

<h2>Resultados de las Pruebas de Hipótesis</h2>
<p><b>Hipótesis 1:</b> La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare NO cambia los sábados lluviosos.</p>
<p>Resultado de la prueba: p-value = {pvalue_hypothesis}</p>

<h2>Conclusiones</h2>")
<p>El analisis mostro que Flash Cab es la empresa con mayor numero de viajes, y Loop es el barrio con mas finalizaciones de viajes.</p>")

"""
report_content = report_content.format(
    pvalue_hypothesis = pvalue_hypothesis
)

# Generar el informe final en HTML
save_report(report_content)