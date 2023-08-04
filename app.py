import shutil
from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import JSONResponse
import os
from config import foldersDirectory

app = FastAPI()

def save_uploaded_file(upload_file: UploadFile, destination_path: str):
    with open(destination_path, "wb") as file:
        shutil.copyfileobj(upload_file.file, file)

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_file_if_not_exists(directory):
    if not os.path.exists(directory):
        try:
            # Create an empty file without opening it
            os.open(directory, os.O_CREAT)
            return True
        except Exception as e:
            print("Error creating file:", e)
            return False

@app.get("/hello/")
async def hello():
    return {"message": f"Hello World"}

@app.post("/copy/")
async def copy(file_name: str = Form(...),from_where: str = Form(...),to_where: str = Form(...)):
    try:
        if len(to_where) == 1:
            folders = ()
        elif "/" not in to_where:
            folders = (to_where,)
        else:
            folders = os.path.split(to_where[1:])
        
        current_path = "./"+foldersDirectory

        # Create the nested directories
        for folder in folders:
            current_path = os.path.join(current_path, folder)
            create_directory_if_not_exists(current_path)
        if(from_where!='/'):
            from_where = from_where+'/'
        
        source = os.getcwd()+"/"+foldersDirectory+from_where+file_name
        destination = os.getcwd()+"/"+foldersDirectory+to_where

        # If the source is a directory, copy it to the destination
        if os.path.isdir(source) and os.path.isdir(destination):
            destination_path = os.path.join(destination, file_name)
            shutil.copytree(source, destination_path)
            print(f"Folder '{source}' copied to '{destination}'")
        # If the source is a file, copy it to the destination
        else:
            print(file_name,"file")
            print(source,destination)
            shutil.copy(source, destination)
            print(f"File '{source}' copied to '{destination}'")


        return JSONResponse(content={"message": "File copied successfully"}, status_code=200)
    except Exception as e:
        print("hata:",e)
        return JSONResponse(content={"message": str(e)}, status_code=500)

@app.post("/move/")
async def rename(file_name: str = Form(...),from_where: str = Form(...),to_where: str = Form(...)):
    try:
        if len(to_where) == 1:
            folders = ()
        elif "/" not in to_where:
            folders = (to_where,)
        else:
            folders = os.path.split(to_where[1:])
        create_directory_if_not_exists(os.path.join(foldersDirectory)) 
        current_path = "./"+foldersDirectory
        # Create the nested directories
        for folder in folders:
            current_path = os.path.join(current_path, folder)
            create_directory_if_not_exists(current_path)

        if(from_where!='/'):
            from_where = from_where+'/'
          
        source = os.getcwd()+"/"+foldersDirectory+from_where+file_name
        destination = os.getcwd()+"/"+foldersDirectory+to_where
      
        # If the source is a directory, copy it to the destination
        if os.path.isdir(source) and os.path.isdir(destination):
            destination_path = os.path.join(destination, file_name)
            shutil.move(source, destination_path)
            print(f"Folder '{source}' moved to '{destination}'")
        # If the source is a file, copy it to the destination
        else:
            shutil.move(source, destination)
            print(f"File '{source}' moved to '{destination}'")

        return JSONResponse(content={"message": "File moved successfully"}, status_code=200)
    except Exception as e:
        print("hata:",e)
        return JSONResponse(content={"message": str(e)}, status_code=500)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), file_path: str = Form(...)):
    try:
        # Split the directory into individual folders
        if len(file_path) == 1:
            folders = ()
        elif "/" not in file_path:
            folders = (file_path,)
        else:
            folders = os.path.split(file_path)

        current_path = "./"+foldersDirectory
        # Create the nested directories
        for folder in folders:
            current_path = os.path.join(current_path, folder)
            create_directory_if_not_exists(current_path)

        # Create given file into the current_path
        path_parts = file.filename.split('/')
        last_part = path_parts[-1]

        save_path = f"{current_path}/{last_part}" 
        save_uploaded_file(file, save_path)      

        return JSONResponse(content={"message": "File saved successfully"}, status_code=200)
    except Exception as e:
        print("hata:",e)
        return JSONResponse(content={"message": str(e)}, status_code=500)

@app.post("/rename/")
async def rename(old_name: str = Form(...),new_name: str = Form(...),path: str = Form(...)):
    try:
        current_path = os.getcwd()+"/"+foldersDirectory
        old_file_path = os.path.join(current_path+path, old_name)
        new_file_path = os.path.join(current_path+path, new_name)

        os.rename(old_file_path, new_file_path)
        return JSONResponse(content={"message": "File renamed successfully"}, status_code=200)
    except Exception as e:
        print("hata:",e)
        return JSONResponse(content={"message": str(e)}, status_code=500)

@app.post("/delete/")
async def rename(file_name: str = Form(...),location: str = Form(...)):
    try:
        current_path = os.getcwd()+"/"+foldersDirectory
        #remove the incoming file_name in location
        if(location!='/'):
            location = location+'/'
        filePath = os.path.join(current_path+location+file_name)
        pathInDirectory = "/"+foldersDirectory+location+file_name

        if(not (os.path.exists(filePath))):
            print("file not found to delete!",pathInDirectory)
        else:
            if(os.path.isdir(filePath)):
                shutil.rmtree(filePath)
            else:
                os.remove(filePath)

        return JSONResponse(content={"message": "File deleted successfully"}, status_code=200)
    except Exception as e:
        print("dosya silinirken hata oluştu:",pathInDirectory)
        return JSONResponse(content={"message": str(e)}, status_code=500)

@app.post("/create-folder/")
async def createFolder(file_name: str = Form(...),location: str = Form(...)):
    try:
        current_path = os.getcwd()+"/"+foldersDirectory+location
        current_path = os.path.join(current_path, file_name)
        create_directory_if_not_exists(current_path)
        return JSONResponse(content={"message": "Folder created successfully"}, status_code=200)
    except Exception as e:
        print("hata:",e)
        return JSONResponse(content={"message": str(e)}, status_code=500)

@app.post("/create-file/")
async def createFolder(file_name: str = Form(...),location: str = Form(...)):
    try:
        if(location!='/'):
            location = '/'+location
        current_path = os.getcwd()+"/"+foldersDirectory+location
        current_path = os.path.join(current_path, file_name)
        create_file_if_not_exists(current_path)
        return JSONResponse(content={"message": "File created successfully"}, status_code=200)
    except Exception as e:
        print("hata:",e)
        return JSONResponse(content={"message": str(e)}, status_code=500)

