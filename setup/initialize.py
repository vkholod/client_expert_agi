import os
import sys
import boto3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

REQUIRED_ENV_VARS = [
    "GEMINI_API_KEY"
]

FOLDERS_TO_CREATE = [
    "data",
    "logs"
]


def check_env_vars():
    print("Checking environment variables...")
    missing = []
    for var in REQUIRED_ENV_VARS:
        if not os.getenv(var):
            missing.append(var)
    if missing:
        print(f"Missing required environment variables: {', '.join(missing)}")
        sys.exit(1)
    print("All required environment variables are present.")


def create_folders():
    print("Creating required folders...")
    for folder in FOLDERS_TO_CREATE:
        Path(folder).mkdir(parents=True, exist_ok=True)
        print(f"  - Ensured folder exists: {folder}")
    print("Folder setup complete.")


def main():
    print("Starting agent setup...\n")
    check_env_vars()
    create_folders()
    print("\nInitialization complete. Ready to run agent!")


if __name__ == "__main__":
    main()
