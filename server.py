from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from rembg import remove
import os
import uuid
import shutil

app = FastAPI()

# CORS config - Allow your frontend URL here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace "*" with your specific frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory setup
STORAGE_DIR = "storage"
PROCESSED_DIR = "processed"
os.makedirs(STORAGE_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    # Generate unique filenames
    filename_only = os.path.splitext(file.filename)[0]
    # Clean filename of spaces for URL safety
    clean_name = filename_only.replace(" ", "_")
    unique_id = uuid.uuid4().hex[:8]
    
    save_name = f"{unique_id}_{clean_name}{os.path.splitext(file.filename)[1]}"
    process_name = f"{unique_id}_{clean_name}.png"

    orig_path = os.path.join(STORAGE_DIR, save_name)
    processed_path = os.path.join(PROCESSED_DIR, process_name)

    try:
        # 1. Save original file
        with open(orig_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # 2. Remove background
        with open(orig_path, "rb") as f:
            input_bytes = f.read()
            output_bytes = remove(input_bytes)

        # 3. Save processed file
        with open(processed_path, "wb") as f:
            f.write(output_bytes)

        return {
            "status": "success",
            "original": f"/storage/{save_name}",
            "processed": f"/processed/{process_name}"
        }

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Image processing failed")

@app.get("/storage/{filename}")
async def get_original(filename: str):
    path = os.path.join(STORAGE_DIR, filename)
    if os.path.exists(path):
        return FileResponse(path)
    raise HTTPException(status_code=404, detail="File not found")

@app.get("/processed/{filename}")
async def get_processed(filename: str):
    path = os.path.join(PROCESSED_DIR, filename)
    if os.path.exists(path):
        return FileResponse(path)
    raise HTTPException(status_code=404, detail="File not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)