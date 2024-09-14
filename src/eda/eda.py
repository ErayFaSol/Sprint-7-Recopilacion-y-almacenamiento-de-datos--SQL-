# eda.py
import matplotlib.pyplot as plt
import os

# Crear la carpeta 'images' si no existe
if not os.path.exists('images'):
    os.makedirs('images')
def plot_top_10_taxi_company(df, filename='taxi_company.png'):
    top_10_taxi_company = df.head(10)
    plt.figure(figsize=(12,6))
    plt.bar(top_10_taxi_company['company_name'], top_10_taxi_company['trips_amount'])
    plt.xticks(rotation=90)
    plt.xlabel('Empresa de taxis')
    plt.ylabel('Numero de viajes')
    plt.title('Numero de viajes por empresa de Taxis')
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()  # Cerrar la figura para evitar que se mantenga en memoria

def plot_top_10_dropoff(df, filename='dropoff_locations.png'):
    top_10_dropoff = df.sort_values(by='average_trips', ascending=False).head(10)
    plt.figure(figsize=(12,6))
    plt.bar(top_10_dropoff['dropoff_location_name'], top_10_dropoff['average_trips'])
    plt.xticks(rotation=90)
    plt.xlabel('Barrio de Finalización del Viaje')
    plt.ylabel('Promedio de Viajes')
    plt.title('Top 10 Barrios por Promedio de Finalizaciones de Viaje')
    plt.savefig('images/' + filename)  # Guardar gráfica como imagen
    plt.close()
