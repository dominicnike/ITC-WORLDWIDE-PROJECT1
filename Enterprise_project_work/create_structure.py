import os

# Define the folder structure
folder_structure = {
    "EnterprisePythonSolution": {
        "Section1_BigData_Workflow": {
            "Task1_ETL_Pipeline": ["etl_pipeline.py", "README.md"],
            "Task2_WebScraping": ["web_scraping_workflow.py", "airflow_dag.py", "README.md"],
        },
        "Section2_DataAnalysis_BI": {
            "Task3_API_Integration": ["api_integration.py", "README.md"],
            "Task4_BI_Dashboard": {
                "PowerBI": ["dashboard.pbix", "README.md"]
            },
        },
        "Section3_DevOps_Cloud": {
            "Task5_Deployment": {
                "terraform": ["main.tf", "README.md"],
                "files": ["ci_cd_pipeline.yaml", "README.md"]
            },
            "Task6_Security": ["security_architecture.md", "README.md"],
        },
        "README.md": None,
    }
}

# Function to create folders and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create folder
            os.makedirs(path, exist_ok=True)
            # Recursively create subfolders and files
            create_structure(path, content)
        elif isinstance(content, list):
            # Create folder and files
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                file_path = os.path.join(path, file_name)
                with open(file_path, "w") as f:
                    f.write("")  # Create an empty file
        elif content is None:
            # Create a single file
            with open(path, "w") as f:
                f.write("")  # Create an empty file

# Create the folder structure
base_directory = os.getcwd()  # Current working directory
create_structure(base_directory, folder_structure)

print("Folder structure created successfully!")