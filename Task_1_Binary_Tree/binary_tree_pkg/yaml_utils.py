import yaml
from .node import Node

def build_tree_from_yaml(filepath):
    """Parses a YAML file and generates a tree."""
    try:
        with open(filepath, 'r') as f:
            data = yaml.safe_load(f)
        return _dict_to_node(data)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return None

def _dict_to_node(data):
    if data is None or 'value' not in data:
        return None
    
    node = Node(data['value'])
    
    if 'left' in data:
        node.left = _dict_to_node(data['left'])
    if 'right' in data:
        node.right = _dict_to_node(data['right'])
        
    return node

def save_tree_to_yaml(root, filepath):
    """Writes the binary tree data into a YAML file."""
    data = _node_to_dict(root)
    with open(filepath, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

def _node_to_dict(node):
    if node is None:
        return None
    
    data = {'value': node.value}
    
    # Only adding left/right if they exist to keep YAML clean
    left_node = _node_to_dict(node.left)
    if left_node:
        data['left'] = left_node
        
    right_node = _node_to_dict(node.right)
    if right_node:
        data['right'] = right_node
        
    return data
