# FastAPI File Management Project

Welcome!

This README file provides instructions on how to set up and run to this application.

This application is a file management platform. Incoming requests to the APIs handle operations such as creating, deleting, updating, moving, and copying files or folders within the path specified in the config file.

<hr>
<br>

## Installation and Run
<br>

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/fastapi-project.git
    ```
2. Go to the project directory:
   ```bash
   cd fastapi-project
    ```
    <br>

    ### | WITH DOCKER

    3. Create a virtual environment (optional but recommended):
        ```bash
        docker compose up --build
        ```
        Then app will run in 8000 port. You can change the port in docker files.
    
    <br>

    ### | WITHOUT DOCKER

    3. Go to the project directory:
        ```bash
        cd app
        ```

    4. Create a virtual environment (optional but recommended):
        ```bash
        python3 -m venv venv
        ```

    5. Install dependencies from requirements.txt:
        ```bash
        pip3 install -r requirements.txt
        ```

    6. Run the application

        <br>
        FastAPI projects are usually started using "uvicorn" from the terminal. In this project, the main function in the main.py file performs this operation. Therefore, you only need to write the following command in the terminal

        <br>

        ```bash
        python3 main.py
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
Edit the config.py file to configure your application settings for run without docker.
You can change settings in docker files to run with docker.

<br>

<br>
<hr><hr>

<img src="readme.svg" width="800" height="400">

<hr><hr>