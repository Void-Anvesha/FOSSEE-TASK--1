# Standard Operating Procedure (SOP) - FOSSEE Assignment

This document outlines the detailed steps to set up, install, and execute the tasks included in this assignment.

## Directory Structure
- `Task_1_Binary_Tree/`: Contains the Python package for binary tree operations.
- `Task_2_Blender_Addon/`: Contains the Blender add-on script.

---

## Task 1: Binary Tree Package

### 1. Overview
This task implements a Python package (`binary_tree_pkg`) to create, manipulate, and visualize binary trees. It supports:
- Adding nodes by path (e.g., "Left-Right").
- Visualizing the tree structure in the console.
- Saving/Loading tree structures to/from YAML files.

### 2. Prerequisites
- **Python 3.6+** must be installed on your system.
- **pip** (Python package installer).

### 3. Setup & Installation
1. Open your terminal or command prompt.
2. Navigate to the `Task_1_Binary_Tree` directory:
   ```powershell
   cd "Task_1_Binary_Tree"
   ```
   *(Adjust the path if you are not in the root directory)*
3. Install the required dependencies (PyYAML):
   ```powershell
   pip install -r requirements.txt
   ```

### 4. Execution
To run the main demonstration script which showcases all features:

```powershell
python main.py
```

**Expected Output:**
- Examples of creating a hardcoded tree.
- A dynamically modified tree using path-based insertion.
- The tree structure printed to the console.
- A demonstration of saving the tree to `output.yaml` and loading from `test.yaml`.

---

## Task 2: Blender Addon (Cube Generator)

### 1. Overview
A Blender add-on that generates `N` cubes in a grid pattern and provides functionality to merge them into a single mesh if they share common faces.

### 2. Prerequisites
- **Blender 3.0** or newer is recommended (Script verified for Blender 3.0 API).

### 3. Installation
1. Open Blender.
2. Navigate to **Edit** → **Preferences**.
3. Select the **Add-ons** tab on the left.
4. Click the **Install...** button at the top right.
5. Browse to the file:
   `Task_2_Blender_Addon/cube_generator_addon.py`
6. Click **Install Add-on**.
7. **Enable** the add-on by checking the checkbox next to **Object: Cube Generator & Merger**.

### 4. Usage
1. In the **3D Viewport**, press the `N` key on your keyboard to toggle the **Sidebar** (on the right side of the view).
2. Click on the tab labeled **Task 1** (as defined in the script).
3. **Panel Controls**:
   - **Number of N**: Set the number of cubes to generate.
   - **Rows / Cols**: Define the grid layout dimensions.
4. **Operations**:
   - **Distribute Cubes**: Generates the cubes in the scene.
   - **Delete Cubes**: Deletes selected cubes.
   - **Compose Mesh** (Merge): Select multiple cubes (Shift+Click) and click this to merge them. *Note: Cubes must be touching to effectively merge geometry.*
