import os, sys
from pathlib import Path
import logging

while True:
    project_name = input("Enter Project Name:")
    if project_name != "":
        break

list_of_files = [
    f"{project_name}/__init.py__",
    f"{project_name}/components/__init.py__",
    f"{project_name}/config/__init.py__",
    f"{project_name}/constants/__init.py__",
    f"{project_name}/entity/__init.py__",
    f"{project_name}/exception/__init.py__",
    f"{project_name}/logger/__init.py__",
    f"{project_name}/pipeline/__init.py__",
    f"{project_name}/utils/__init.py__",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py"
]

for filePath in list_of_files:
    filePath = Path(filePath)
    fileDir, fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
    
    if not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
        with open(filePath, "w") as f:
            pass
    else:
        logging.info(f"File is already present at: {filePath}.")