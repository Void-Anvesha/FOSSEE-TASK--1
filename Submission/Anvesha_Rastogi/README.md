# FOSSEE Screening Task Submission

## Author
Anvesha Rastogi

## Directory Structure
- `Task 1/`: Contains the Binary Tree Python package and test script.
- `Task 2/`: Contains the Blender Addon script.
- `Resume.pdf`: (Please install/replace with your actual resume)
- `SOP.pdf`: (Please install/replace with your actual SOP)

## Task 1: Binary Tree Implementation

### Prerequisites
- Python 3.x
- pip

### Installation
1. Navigate to the `Task 1` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Test Script
Run the `main.py` script to verify Feature Set 1 and 2:
```bash
python main.py
```
This will:
- Create a binary tree and demonstrate operations (add, print).
- Load a tree from `test.yaml`.
- Save the tree to `output.yaml`.

### Features
- **Binary Tree**: Full implementation of Node class and helpers.
- **YAML Integration**: `build_tree_from_yaml` and `save_tree_to_yaml`.
- **Bonus**: The `Node` class is designed to support General Trees (n-ary) via a `children` list, while maintaining specific `left`/`right` properties for binary tree compatibility.

## Task 2: Blender Addon

### Installation
1. Open Blender (3.0+ recommended).
2. Go to **Edit -> Preferences -> Add-ons**.
3. Click **Install...** and select `cube_generator_addon.py` from the `Task 2` folder.
4. Enable the addon "Cube Generator & Merger".

### Usage
The addon panel is located in the **3D Viewport Sidebar (N-panel)** under the **Task 1** tab (as per screenshot reference, labeled "Task 1" in UI).

#### Feature Set 1
- **Number of N**: Input the number of cubes (Must be <= 20).
- **Distribute Cubes**: Generates cubes in a grid pattern.
- **Delete Cubes**: Deletes selected cubes.

#### Feature Set 2
- **Compose Mesh** (Merge): Select at least 2 cubes/meshes that share a face and click "Compose Mesh". This will join them, merge vertices, and remove interior faces.

