import os

base_dir = "AI-Agentic AI Data Cleaner v2.0"
structure = {
    "agents": ["cleaner.py", "validator.py", "enricher.py"],
    "loaders": ["csv_loader.py", "db_loader.py", "api_loader.py"],
    "pipelines": ["clean_pipeline.py"],
    "rules": ["basic_rules.py"],
    "services": ["clean_service.py"],
    "app": ["app.py"],
    "tests": [],
    "": ["main.py", "requirements.txt", "README.md", ".env"]
}

# Create directories and files
for folder, files in structure.items():
    dir_path = os.path.join(base_dir, folder)
    os.makedirs(dir_path, exist_ok=True)

    for file in files:
        file_path = os.path.join(dir_path, file)
        with open(file_path, "w") as f:
            f.write(f"# {file} - Placeholder\n")

print("✅ Project folder structure created successfully!")
