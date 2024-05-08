import json
import yaml

def json_to_yaml(json_file, yaml_file):
    # Leer el archivo JSON
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    
    # Convertir JSON a YAML
    with open(yaml_file, 'w') as f:
        yaml.dump(json_data, f, default_flow_style=False)

# Ejemplo de uso
json_file = 'data.json'
yaml_file = 'data.yaml'
json_to_yaml(json_file, yaml_file)
