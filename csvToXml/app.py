import pandas as pd
from dicttoxml import dicttoxml

def df_to_xml_from_csv(archivo_csv, nombre_archivo_xml, root_name='data', record_name='record'):
    # Leer el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_csv)
    
    # Convertir el DataFrame a un diccionario de Python
    data_dict = df.to_dict(orient='records')
    
    # Convertir el diccionario a XML
    xml_data = dicttoxml(data_dict, custom_root=root_name, item_func=lambda x: record_name)
    
    # Escribir los datos XML en un archivo
    with open(nombre_archivo_xml, 'wb') as f:
        f.write(xml_data)

# Ejemplo de uso
df_to_xml_from_csv('data.csv', 'datos.xml', 'root', 'row')
df_to_xml_from_csv('data_2.csv', 'datos_2.xml')
