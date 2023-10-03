# PyLintPushBot

PyLintPushBot is a Python utility that automates the process of linting and pushing Python code to a GitHub repository. It utilizes the Black code formatter for auto-formatting Python files and GitPython for handling Git operations. This tool is designed to streamline code quality maintenance in your GitHub projects.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running PyLintPushBot](#running-pylintpushbot)

## Getting Started

### Prerequisites

Before using PyLintPushBot, ensure that you have the following prerequisites installed:

- Python 3.x
- Pip (Python package manager)

### Installation

To maintain a clean and isolated development environment, it is recommended to set up a virtual environment. Follow these steps to get started:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/dgamee/PyLintPushBot.git
2. Navigate to the project directory:

    ```bash
    cd PyLintPushBot
3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    - ### Windows:
      ```shell
      .\.venv\Scripts\activate
      ```

   - ### Linux/macOS:
     ```shell
     source .venv/bin/activate
5. Install the required Python packages using pip:
    ```shell
    pip install -r requirements.txt
## Usage

### Configuration
Before running PyLintPushBot, you need to configure the necessary environment variables in a `.env `file. Create a ``.env`` file in the project root directory and add the following information:

```shell
REPO_PATH=/path/to/your/repo
GITHUB_USERNAME=your_username
GITHUB_TOKEN=your_personal_access_token
```
- REPO_PATH: The path to the local Git repository you want to push changes to.
- GITHUB_USERNAME: Your GitHub username.
- GITHUB_TOKEN: Your personal access token with the required permissions to push to the repository.

### Running PyLintPushBot
Once you have configured the environment variables and set up the virtual environment, you can run PyLintPushBot from the command line. Provide the Python files you want to format and push as command-line arguments:

```
python linter.py file1.py file2.py
```
PyLintPushBot will automatically format the specified Python files using Black and push the changes to your GitHub repository.