import yaml
import xml.etree.ElementTree as ET

def yaml_to_xml(yaml_file, xml_file, root_name='data', record_name='record'):
    # Leer el archivo YAML
    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)
    
    # Crear el elemento raíz del XML
    root = ET.Element(root_name)

    # Convertir YAML a XML recursivamente
    def yaml_to_xml_recursive(data, parent):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict) or isinstance(value, list):
                    new_parent = ET.SubElement(parent, key)
                    yaml_to_xml_recursive(value, new_parent)
                else:
                    field = ET.SubElement(parent, key)
                    field.text = str(value)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, dict) or isinstance(item, list):
                    yaml_to_xml_recursive(item, parent)
                else:
                    field = ET.SubElement(parent, record_name)
                    field.text = str(item)
    
    # Convertir YAML a XML
    yaml_to_xml_recursive(yaml_data, root)

    # Crear el árbol XML
    tree = ET.ElementTree(root)
    
    # Guardar el XML en un archivo
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)
    print(f"El archivo '{xml_file}' se ha creado con éxito.")

# Ejemplo de uso
yaml_file = 'data.yaml'
xml_file = 'data.xml'
yaml_to_xml(yaml_file, xml_file)
