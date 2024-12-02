import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

list_of_files = [
    ".github/workflows",
    "src/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_tranformation.py",
    "src/components/model_traines.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "py_project.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
    "src/database/mongodb_connection.py",
    "src/database/mogodb_crud.py",
    "src/database/__init__.py",
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create the directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    # Create the file if it does not exist or if it is empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass # Create empty file
        logging.info(f"Created empty file: {filepath}")
