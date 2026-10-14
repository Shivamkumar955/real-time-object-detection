
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.detector import detect_objects

import cv2
import numpy as np


app = FastAPI(
    title="Real-Time Object Detection API",
    description="YOLO-based image object detection",
    version="1.0.0"
)


# Allow the local frontend to connect to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return {
        "message": "Real-Time Object Detection API is running"
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read uploaded image
    image_bytes = await file.read()

    # Convert bytes into an OpenCV image
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid image file"}
        )

    # Run YOLO detection
    detections = detect_objects(image)

    return {
        "filename": file.filename,
        "total_objects": len(detections),
        "detections": detections
    }
