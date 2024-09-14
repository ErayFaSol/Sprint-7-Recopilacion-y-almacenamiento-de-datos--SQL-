# main.py
from preprocessing.preprocessing import load_data, inspect_data, clean_data
from eda.eda import plot_top_10_taxi_company, plot_top_10_dropoff
from hypothesis_testing.hypothesis_testing import hypothesis_test
from utils.generate_report import save_report_as_html

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
hypothesis_test(good_weather, bad_weather)
# Generar el informe final en HTML
save_report_as_html()