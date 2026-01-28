from .node import Node

def create_tree(root_value):
    """Creates a new binary tree with a root node."""
    return Node(root_value)

def add_node_by_path(root, path, value):
    """
    Adds a node to the binary tree following the path 'L' (Left) / 'R' (Right).
    path: string, e.g., "LR" means Left child's Right child.
    """
    current = root
    for char in path[:-1]:
        if char.upper() == 'L':
            if current.left is None:
                current.left = Node(None) # Create intermediate if missing? Or error? 
                # Prompt implies valid paths or simple addition. 
                # Let's assume user provides path to valid parent.
                # If parent is None, we can't traverse. 
                # But for robustness let's create placeholders if we strictly follow path addition
                pass 
            current = current.left
        elif char.upper() == 'R':
            if current.right is None:
                current.right = Node(None)
            current = current.right
        
    # Last char determines where to put the new value
    if path[-1].upper() == 'L':
        current.left = Node(value)
    elif path[-1].upper() == 'R':
        current.right = Node(value)

def delete_tree(root):
    """Deletes the entire tree (Python GC handles it, but we can clear references)."""
    if root:
        root.children = []
        # In C++ we'd delete. In Python, removing refs is enough.
        # We can set root properties to None to be sure.

def delete_node(root, value):
    """
    Deletes a node with the specific value.
    Strategy: Find node, remove reference from parent.
    Note: deeper children are lost.
    """
    if root is None:
        return
    
    # Check children
    if root.left and root.left.value == value:
        root.left = None
        return
    if root.right and root.right.value == value:
        root.right = None
        return

    delete_node(root.left, value)
    delete_node(root.right, value)

def edit_node(root, old_value, new_value):
    """Finds a node with old_value and updates it to new_value."""
    if root is None:
        return
    if root.value == old_value:
        root.value = new_value
        return
    edit_node(root.left, old_value, new_value)
    edit_node(root.right, old_value, new_value)

def print_tree(root, level=0, prefix="Root:"):
    """
    Prints the tree in the format:
    Root:1
     L---2
     R---3
    """
    if root is None:
        return
    
    print(f"{' ' * level}{prefix}{root.value}")
    
    if root.left:
        print_tree(root.left, level + 1, "L---")
    if root.right:
        print_tree(root.right, level + 1, "R---")
    
    # helper for general tree (Bonus)
    # If there are more children (index > 1)
    if len(root.children) > 2:
        for i in range(2, len(root.children)):
             if root.children[i]:
                print_tree(root.children[i], level + 1, f"C{i}---")
