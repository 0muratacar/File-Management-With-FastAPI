import os
from app import app as fastapi_app
from config import foldersDirectory, host, port
def initialize():
    print("Initializing the application...")
    if not os.path.exists('./'+foldersDirectory):
        os.mkdir(foldersDirectory)
        os.chmod('./'+foldersDirectory, 0o777)


if __name__ == "__main__":
    initialize()
    import uvicorn
    uvicorn.run(fastapi_app, host=host, port=port)
