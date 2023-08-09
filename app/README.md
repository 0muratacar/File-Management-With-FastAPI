# FastAPI File Management Project

Welcome!

This README file provides instructions on how to set up and run to this application.

This application is a file management platform. Incoming requests to the APIs handle operations such as creating, deleting, updating, moving, and copying files or folders within the path specified in the config file.

<hr>
<br>

## Installation
<br>

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-project.git
    ```
2. Go to the project directory:
   ```bash
   cd fastapi-project
    ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
    ```
4. Install dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
    ```

<br>

## Directory Structure
<br>

* main.py: The main FastAPI application.
* app.py: Includes the APIs for file operations.
* config.py: Configuration settings for the application.
* requirements.txt: List of required Python packages.


<br>

## Configuration
<br>
Edit the config.py file to configure your application settings.

<br>

## Running the Application
<br>
FastAPI projects are usually started using "uvicorn" from the terminal. In this project, the main function in the main.py file performs this operation. Therefore, you only need to write the following command in the terminal

<br>

```bash
python main.py
```

<br>
<hr><hr>
THANKS
<hr><hr>