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
        #make a gitignore file automatically incase the user decides to use git add .
        gitignore_updated = False
        gitignore_content = [
            ".env", 
            "linter.py", 
            ".venv"
            #add more files to ignore
            ]

        with open(".gitignore", "a") as gitignore_file:
            for pattern in gitignore_content:
                gitignore_file.write(pattern + "\n")

        if not gitignore_updated:
            print(".gitignore file has been created or updated.")
            gitignore_updated = True
    except ImportError:
        print("GitPython is not installed. Please install it.")
        return

    repo = git.Repo(repo_path)
    
    for python_file in python_files:
        repo.git.add(python_file)
        #can also use *.py, *.sh to add all py or sh files
    
    #user can write own commit message or leave blank to use default message
    commit_option = input("Choose commit option (1: Write commit message, 2: Use default message): ")

    if commit_option == "1":
        message = input("Commit message: ")
    elif commit_option == "2":
        message = "Auto-format using autopep8"
    else:
        print("Invalid option selected. Using default commit message.")
        message = "Auto-format using autopep8"
        
    repo.git.commit("-m", message)
    
    #handle push errors
    try:
        repo.remotes.origin.push()
        print("Changes committed and pushed successfully.")
    except git.exc.GitCommandError as e:
        error_message = str(e)
        if "fatal: no upstream" in error_message:
            repo.git.push("--set-upstream", "origin", "main")
        elif "failed to push some refs" in error_message:
            repo.git.pull()
            repo.git.push()
        else:
            print("An error occurred while pushing to the repository.")
            raise
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    print("Linting and pushing to GitHub completed.")

if __name__ == "__main__":
    main()