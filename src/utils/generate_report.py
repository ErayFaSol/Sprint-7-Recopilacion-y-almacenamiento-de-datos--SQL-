# generate_report.py
def save_report_as_html():
    with open("reporte_final.html", "w") as file:
        # Título del reporte
        file.write(f"<h1>Reporte Final de Analisis</h1>")
        
        # Grafica 1: Empresas de taxi y numero de viajes
        file.write(f"<h2>Grafico: Numero de Viajes por Empresa de Taxis</h2>")
        file.write(f'<img src="images/taxi_company.png" alt="Grafico de Empresas de Taxis y Numero de Viajes">')

        # Grafica 2: Barrios por Promedio de Finalizacion de Viajes
        file.write(f"<h2>Grafico: Top 10 Barrios por Promedio de Finalizacion de Viajes</h2>")
        file.write(f'<img src="images/dropoff_locations.png" alt="Grafico de Top 10 Barrios por Promedio de Finalizacion">')

        # Conclusiones
        file.write(f"<h2>Conclusiones</h2>")
        file.write(f"<p>El analisis mostro que Flash Cab es la empresa con mayor numero de viajes, y Loop es el barrio con mas finalizaciones de viajes.</p>")
