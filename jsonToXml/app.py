import json
import xml.etree.ElementTree as ET

def json_to_xml(json_file, nombre_archivo_xml, root_name='data', record_name='record'):
    # Leer el archivo JSON
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    
    # Crear el elemento raíz del XML
    root = ET.Element(root_name)
    
    # Convertir el JSON en XML recursivamente
    def json_to_xml_recursive(data, parent):
        if isinstance(data, dict):
            for key, value in data.items():
                # Si el valor es un diccionario o una lista, crear un nuevo elemento
                if isinstance(value, dict) or isinstance(value, list):
                    new_parent = ET.SubElement(parent, key)
                    json_to_xml_recursive(value, new_parent)
                else:
                    # Si el valor es un dato simple, agregarlo como texto al elemento actual
                    new_element = ET.SubElement(parent, key)
                    new_element.text = str(value)
        elif isinstance(data, list):
            for item in data:
                # Si el elemento de la lista es un diccionario o una lista, crear un nuevo elemento
                if isinstance(item, dict) or isinstance(item, list):
                    json_to_xml_recursive(item, parent)
                else:
                    # Si el elemento de la lista es un dato simple, agregarlo como texto al elemento actual
                    new_element = ET.SubElement(parent, record_name)
                    new_element.text = str(item)
    
    # Convertir el JSON en XML recursivamente
    json_to_xml_recursive(json_data, root)
    
    # Crear el árbol XML
    tree = ET.ElementTree(root)
    
    # Guardar el XML en un archivo
    tree.write(nombre_archivo_xml, encoding='utf-8', xml_declaration=True)

# Ejemplo de uso
json_file = 'data.json'
nombre_archivo_xml = 'data.xml'
json_to_xml(json_file, nombre_archivo_xml)
