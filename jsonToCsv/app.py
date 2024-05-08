import pandas as pd
import json

def flatten_json(data):
    flattened = {}
    for key, value in data.items():
        if isinstance(value, dict):
            flattened[key] = json.dumps(value)
        else:
            flattened[key] = value
    return flattened

def generar_csv_pandas(nombre_lista_json, nombre_archivo_json, nombre_archivo_csv, separador=',', headers=None):
    # Leer el archivo JSON
    with open(nombre_archivo_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Obtener el título dinámicamente según los encabezados proporcionados
    title = None
    for header in headers:
        if header in data[nombre_lista_json]:
            title = data[nombre_lista_json][header]
            break

    # Obtener el contenido del glossary
    glossary = flatten_json(data[nombre_lista_json])

    # Crear el diccionario de datos dinámicamente
    data_dict = {}
    for header in headers:
        if header in glossary:  # Verificar si el encabezado está presente en el glossary
            data_dict[header] = [glossary[header]]
        else:
            data_dict[header] = [""]  # Si el encabezado no está presente, agregar una celda vacía

    # Crear DataFrame
    df = pd.DataFrame(data_dict)

    # Guardar el DataFrame como archivo CSV
    df.to_csv(nombre_archivo_csv, sep=separador, index=False, header=headers is not None)

# Ejemplo de uso con encabezados especificados
generar_csv_pandas('GlossEntry', 'example_1.json', 'example_1.csv', headers=["ID", "SortAs"])


# Ejemplo de uso con encabezados especificados
# generar_csv_pandas('company', 'example_3.json', 'example_3.csv', headers=["name", "employees", "departments"])

# generar_csv_pandas('employees', 'example_2.json', 'example_2.csv', headers=["title", "employee1", "employee2"])

generar_csv_pandas('GlossEntry', 'example_1.json', 'example_1.csv', headers=["ID", "SortAs"])
