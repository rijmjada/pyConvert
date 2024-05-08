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

def find_title(data, headers):
    # Función para buscar el título dinámicamente según los encabezados proporcionados
    for header in headers:
        title = find_key(data, header)
        if title:
            return title
    return None

def find_key(data, target_key):
    # Función recursiva para encontrar la clave target_key en el JSON data
    if isinstance(data, dict):
        if target_key in data:
            return data[target_key]
        else:
            for value in data.values():
                result = find_key(value, target_key)
                if result:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = find_key(item, target_key)
            if result:
                return result
    return None

def generar_csv_pandas(nombre_lista_json, nombre_archivo_json, nombre_archivo_csv, separador=',', headers=None):
    # Leer el archivo JSON
    with open(nombre_archivo_json, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Obtener el título dinámicamente según los encabezados proporcionados
    title = find_title(data, headers)

    # Obtener el contenido del JSON
    content = flatten_json(find_key(data, nombre_lista_json))

    # Crear el diccionario de datos dinámicamente
    data_dict = {}
    for header in headers:
        if header in content:  # Verificar si el encabezado está presente en el contenido
            data_dict[header] = [content[header]]
        else:
            data_dict[header] = [""]  # Si el encabezado no está presente, agregar una celda vacía

    # Crear DataFrame
    df = pd.DataFrame(data_dict)

    # Guardar el DataFrame como archivo CSV
    df.to_csv(nombre_archivo_csv, sep=separador, index=False, header=headers is not None)

# Ejemplo de uso con encabezados especificados
generar_csv_pandas('departments', 'example_4.json', 'example_4.csv', headers=["computer_science", "electrical_engineering"])
