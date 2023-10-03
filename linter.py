import os
import subprocess
import argparse
import importlib
from dotenv import load_dotenv

REQUIRED_PACKAGES = ["autopep8", "GitPython"]

def install_required_packages():
    for package in REQUIRED_PACKAGES:
        try:
            importlib.import_module(package)
        except ImportError:
            subprocess.check_call(["pip", "install", package])

def main():
    load_dotenv()

    # Check if environment variables are set
    repo_path = os.getenv("REPO_PATH")
    github_username = os.getenv("GITHUB_USERNAME")
    github_token = os.getenv("GITHUB_TOKEN")

    if not all([repo_path, github_username, github_token]):
        print("Please set all required environment variables.")
        return

    parser = argparse.ArgumentParser(description="Auto-lint and push Python files to GitHub.")
    parser.add_argument("python_files", nargs="+", help="Python files to format and push")
    args = parser.parse_args()
    python_files = args.python_files

    # Install required packages
    install_required_packages()

    # Format Python files using Black
    for python_file in python_files:
        subprocess.check_call(["autopep8", "--in-place", "--aggressive", python_file])

    # Commit and push changes to the repository
    try:
        import git
    except ImportError:
        print("GitPython is not installed. Please install it.")
        return

    repo = git.Repo(repo_path)
    
    for python_file in python_files:
        repo.git.add(python_file)
    repo.git.commit("-m", "Auto-format using autopep8")
    repo.remotes.origin.push()
    
    print("Linting and pushing to GitHub completed.")

if __name__ == "__main__":
    main()
