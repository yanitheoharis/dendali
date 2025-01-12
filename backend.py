from fastapi import FastAPI, File, UploadFile, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import numpy as np
from typing import Annotated
import matplotlib.pyplot as plt 
import shutil
from PIL import Image
from io import BytesIO
import os
import json


UPLOAD_DIR = "uploads/"

app: FastAPI = FastAPI()




origins = [
    "http:127.1.0.0", "http://127.0.0.1:5500"
]


# Note: CORS enabled means that the request from the client reach the server but nothing is return -> actions can be executed within a route (problem? how to limit it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def read_root()-> dict:
    print("root path accessed")

    return {"message": f"welcome"}


    
@app.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    print(file.file)

    
    with open(file.file, "wb") as f:
        cont_open = f.read()
        print("Cont open:", cont_open)


    contents = file.file.read() # reads data as 
    print("Contents", contents)
    try:

        upload_dir = "uploads/"
        file_path = upload_dir + file.filename

        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        return JSONResponse(content={"message": "File upload successful", "filename": file.filename})    

    except Exception as e:
        return JSONResponse(status_code=400, content={"detail":str(e)})
        



@app.post("/upload")
async def upload(request: Request):

    data: bytes = await request.body()
    if data:
        os.makedirs(os.path.dirname(UPLOAD_DIR), exist_ok=True)
        file_path = UPLOAD_DIR + "file1.jfif"
        with open(file_path, "wb+") as f:
            print("Writing received data to file")
            f.write(data)


        img = Image.open(BytesIO(data))
        plt.imshow(img)
        plt.show()
    return JSONResponse(content={"message": "bytes delivered"})


