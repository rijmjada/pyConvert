import pandas as pd
import json

def csv_to_json(nombre_archivo_csv, nombre_archivo_json):
    # Leer el archivo CSV
    df = pd.read_csv(nombre_archivo_csv)

    # Convertir el DataFrame a un diccionario
    data = df.to_dict(orient='records')

    # Escribir el diccionario como JSON en un archivo
    with open(nombre_archivo_json, 'w') as f:
        json.dump(data, f, indent=4)

# Ejemplo de uso
# csv_to_json('example_1.csv', 'example_1.json')
# csv_to_json('example_2.csv', 'example_2.json')
csv_to_json('BABA.csv', 'BABA.json')

