# generate_report.py
def save_report_as_html():
    with open("reporte_final.html", "w") as file:
        # Título del reporte
        file.write(f"<h1>Reporte Final de Análisis</h1>")
        
        # Gráfica 1: Empresas de taxi y número de viajes
        file.write(f"<h2>Gráfico: Número de Viajes por Empresa de Taxis</h2>")
        file.write(f'<img src="taxi_company.png" alt="Gráfico de Empresas de Taxis y Número de Viajes">')

        # Gráfica 2: Barrios por Promedio de Finalización de Viajes
        file.write(f"<h2>Gráfico: Top 10 Barrios por Promedio de Finalización de Viajes</h2>")
        file.write(f'<img src="dropoff_locations.png" alt="Gráfico de Top 10 Barrios por Promedio de Finalización">')

        # Conclusiones
        file.write(f"<h2>Conclusiones</h2>")
        file.write(f"<p>El análisis mostró que Flash Cab es la empresa con mayor número de viajes, y Loop es el barrio con más finalizaciones de viajes.</p>")
