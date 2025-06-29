import os

# Define your project folder structure here
FOLDER_STRUCTURE = [
    "frontend/app.py",
    "frontend/__init__.py",
    "backend/main.py",
    "backend/__init__.py",
    "util/utils.py",
    "util/__init__.py",
    "agents/agent.py",
    "agents/planner_tool.py",
    "agents/weather_tool.py",
    "agents/places_tool.py",
    "agents/visa_tool.py",
    "agents/currency_tool.py",
    "agents/translate_tool.py",
    "agents/packing_tool.py",
    "agents/pdf_tool.py",
    "agents/__init__.py",
    "models/model.yaml",
    "models/__init__.py",  # fixed typo here
    "prompts/prompt.py",
    "prompts/__init__.py",  # fixed typo here
    "visa_data/visa_rules.json",
    "visa_data/__init__.py",
    "pdf/outputs/",  # this is a folder
    "pdf/__init__.py",
    "configs/config.py",
    "configs/__init__.py",  # fixed typo here
    "tests/test_agent.py",
    "tests/__init__.py"
]

def create_project_structure(project_root, structure):
    for path in structure:
        full_path = os.path.join(project_root, path)

        # Check if the path ends with a file extension
        if os.path.splitext(path)[1]:  # It's a file
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            if not os.path.exists(full_path):
                with open(full_path, 'w') as f:
                    pass  # create an empty file
            print(f"Created file: {full_path}")
        else:
            os.makedirs(full_path, exist_ok=True)
            print(f"Created folder: {full_path}")

if __name__ == "__main__":
    project_root = os.getcwd()
    print(f"Project Root: {project_root}")
    create_project_structure(project_root, FOLDER_STRUCTURE)
