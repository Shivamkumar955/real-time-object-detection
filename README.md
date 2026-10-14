
# Real-Time Object Detection System

A computer vision application that detects and classifies objects in uploaded images using YOLO11, Python, OpenCV, and FastAPI. It provides a web interface to upload images and view detected object classes, confidence scores, and bounding-box coordinates.

## Features

- **YOLO-based object detection:** Detects supported object classes in images.
- **Image upload:** Upload images through a web interface.
- **Confidence scores:** Displays confidence for each detection.
- **Bounding-box coordinates:** Returns the coordinates of detected objects.
- **REST API:** Provides image inference through FastAPI.
- **Swagger documentation:** Test the API using the interactive documentation.
- **Web interface:** HTML, CSS, and JavaScript frontend.
- **Input validation:** Returns an error for invalid image files.
- **Optional webcam detection:** Run a separate Python script for live camera detection.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| YOLO11 (Ultralytics) | Object detection |
| OpenCV | Image processing |
| NumPy | Image-array processing |
| FastAPI | REST API backend |
| Uvicorn | ASGI server |
| HTML, CSS, JavaScript | Frontend interface |

## Project Structure

```text
real-time-object-detection/
├── backend/
│   ├── main.py
│   ├── detector.py
│   ├── test_yolo.py
│   └── webcam.py
├── data/
│   └── images/
│       └── test.jpg
├── frontend/
│   ├── index.html
│   └── webcam.html
├── outputs/
├── bus.jpg
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.11 recommended
- Git
- Visual Studio Code or another code editor
- Internet connection to install dependencies and download the model

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Shivamkumar955/real-time-object-detection.git
cd real-time-object-detection
```

### 2. Create a virtual environment

For Windows PowerShell:

```powershell
py -3.11 -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If the virtual environment already exists, activate it instead of creating it again.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Download the YOLO model

The `yolo11n.pt` model file may not be included in the Git repository. Download it with:

```powershell
python -c "from ultralytics import YOLO; YOLO('yolo11n.pt')"
```

## Run the Application

Keep the backend and frontend running in separate terminals.

### 1. Start the backend API

From the project root, run:

```powershell
uvicorn backend.main:app --reload
```

Backend URL: http://127.0.0.1:8000

Interactive API documentation: http://127.0.0.1:8000/docs

The root endpoint can be checked at http://127.0.0.1:8000/

### 2. Start the frontend

Open a second terminal in the project root and run:

```powershell
python -m http.server 5500 --directory frontend
```

Open the image detection page in your browser:

http://127.0.0.1:5500/index.html

### 3. Detect objects in an image

1. Click **Choose File**.
2. Select an image from your computer.
3. Click **Detect Objects**.
4. View the detected object classes, confidence scores, and bounding-box coordinates.

The image detection web interface does not require a webcam.

## API Reference

### `GET /`

Checks whether the API is running.

### `POST /predict`

Accepts an image using `multipart/form-data` and returns detected objects.

Example response:

```json
{
  "filename": "test.jpg",
  "detections": [
    {
      "class": "bus",
      "confidence": 0.9422,
      "bounding_box": [
        38.14,
        11.39,
        530.03,
        335.21
      ]
    }
  ],
  "total_objects": 1
}
```

This is an illustrative example. Actual results depend on the image and model predictions.

## Run Image Detection from Python

From the project root, run:

```powershell
python backend/test_yolo.py
```

The script uses the YOLO model to detect objects in the configured test image and saves an annotated image to the output location configured in the script.

## Optional: Run Webcam Detection

To run live detection using an accessible webcam:

```powershell
python backend/webcam.py
```

This optional script requires a working camera. It is not required for image-upload detection.

## Troubleshooting

- **API connection error:** Make sure the backend is running at `http://127.0.0.1:8000`.
- **Frontend page unavailable:** Make sure the frontend server is running on port `5500`.
- **Model file missing:** Download `yolo11n.pt` using the command in the installation section.
- **Dependency errors:** Activate the virtual environment and install packages from `requirements.txt`.
- **CORS error:** Configure FastAPI CORS middleware to allow the local frontend origin, `http://127.0.0.1:5500`.

## Future Improvements

- Display bounding boxes directly on the uploaded image.
- Add object counts grouped by class.
- Support video-file detection through the web interface.
- Add detection history and downloadable reports.
- Evaluate model performance using precision, recall, F1-score, and inference latency.
- Deploy the application to a cloud platform.

## Learning Outcomes

This project demonstrates practical experience with computer vision, pretrained object-detection models, image processing, REST API development, and frontend-backend integration.

## Project Repository

**GitHub:** [Real-Time Object Detection System](https://github.com/Shivamkumar955/real-time-object-detection)

**API documentation (local):** http://127.0.0.1:8000/docs

**Web application (local):** http://127.0.0.1:5500/index.html

## License

No open-source license has been specified yet. Add a license file if you intend to distribute the project under a particular open-source license.
