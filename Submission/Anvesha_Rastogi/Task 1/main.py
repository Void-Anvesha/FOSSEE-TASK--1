from binary_tree_pkg.node import Node
from binary_tree_pkg.tree_utils import *
from binary_tree_pkg.yaml_utils import *

if __name__ == "__main__":
    print("--- Feature Set 1 Tests ---")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print_tree(root)

    print("\n--- Additional Tests ---")
    root = Node(10)
    print("Initial tree:")
    print_tree(root)
    
    # Add nodes using helper
    print("\nAdding nodes:")
    add_node_by_path(root, "L", 5)
    add_node_by_path(root, "R", 15)
    add_node_by_path(root, "LL", 3)
    add_node_by_path(root, "LR", 7)
    add_node_by_path(root, "RL", 12)
    add_node_by_path(root, "RR", 18)
    
    print("\nTree after additions:")
    print_tree(root)

    print("\n--- Feature Set 2 (YAML) Tests ---")
    # Create the test.yaml file first to match the sample
    sample_yaml_data = {
        'value': 10,
        'left': {
            'value': 5,
            'left': {'value': 3},
            'right': {'value': 7}
        },
        'right': {
            'value': 15,
            'right': {'value': 18}
        }
    }
    # We can write this manually or use our save function. 
    # Let's write it manually to strictly test 'load' first.
    yaml_file = "test.yaml"
    with open(yaml_file, 'w') as f:
        yaml.dump(sample_yaml_data, f, default_flow_style=False, sort_keys=False)

    print(f"\nBuilding tree from '{yaml_file}':")
    yaml_tree_root = build_tree_from_yaml(yaml_file)
    
    if yaml_tree_root:
        print("\nTree built from YAML:")
        print_tree(yaml_tree_root)
        
    # Verify Save
    print("\nSaving tree back to 'output.yaml'...")
    save_tree_to_yaml(yaml_tree_root, "output.yaml")
    print("Done.")
