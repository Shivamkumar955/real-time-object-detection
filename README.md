\# Real-Time Object Detection System



A computer vision project that detects and classifies objects in images using \*\*YOLO, OpenCV, Python, and FastAPI\*\*. The application provides a web interface for uploading images and viewing detection results, including object classes, confidence scores, and bounding-box coordinates.



\## Features



\- \*\*YOLO-based detection:\*\* Identifies objects in uploaded images.

\- \*\*Image upload:\*\* Select an image through a simple web interface.

\- \*\*Confidence scores:\*\* Displays the model's confidence for each detection.

\- \*\*Bounding boxes:\*\* Returns the coordinates of detected objects.

\- \*\*REST API:\*\* Provides an endpoint for image inference using FastAPI.

\- \*\*Interactive API documentation:\*\* Test endpoints through Swagger UI.

\- \*\*Web interface:\*\* Built with HTML, CSS, and JavaScript.

\- \*\*Input validation:\*\* Returns an error for invalid image files.



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Main programming language |

| YOLO11 (Ultralytics) | Object detection model |

| OpenCV | Image processing |

| NumPy | Image-array processing |

| FastAPI | REST API backend |

| Uvicorn | API server |

| HTML, CSS, JavaScript | Frontend interface |



\## Project Structure



```text

real-time-object-detection/

├── backend/

│   ├── main.py

│   ├── detector.py

│   ├── test\_yolo.py

│   └── webcam.py

├── data/

│   ├── images/

│   └── videos/

├── frontend/

│   ├── index.html

│   └── webcam.html

├── models/

├── outputs/

├── tests/

├── requirements.txt

├── .gitignore

└── README.md

```



\## Prerequisites



\- Python 3.11 recommended

\- Git

\- Visual Studio Code or another code editor

\- Internet connection for installing dependencies and downloading the model



\## Installation



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR-USERNAME/real-time-object-detection.git

cd real-time-object-detection

```



Replace `YOUR-USERNAME` with your GitHub username.



\### 2. Create a virtual environment



Windows PowerShell:



```powershell

py -3.11 -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



\### 3. Install dependencies



```powershell

python -m pip install --upgrade pip

pip install -r requirements.txt

```



\### 4. Download the YOLO model



The trained model file is not included in the repository. Download the official Ultralytics YOLO11 nano model:



```powershell

python -c "from ultralytics import YOLO; YOLO('yolo11n.pt')"

```



The model will be downloaded to the working directory when required by the code.



\## Run the Application



\### 1. Start the backend



From the project root, run:



```powershell

uvicorn backend.main:app --reload

```



Backend URL: http://127.0.0.1:8000



Swagger API documentation: http://127.0.0.1:8000/docs



Health check: http://127.0.0.1:8000/health



\### 2. Start the frontend



Open a second terminal from the project root and run:



```powershell

python -m http.server 5500 --directory frontend

```



Open the image detection interface in your browser:



http://127.0.0.1:5500/index.html



\### 3. Detect objects



1\. Select an image using the file-upload control.

2\. Click \*\*Detect Objects\*\*.

3\. View the detected classes, confidence scores, and bounding-box coordinates.



\## API Reference



\### `GET /`



Checks whether the API is running.



\### `GET /health`



Returns the API health status.



\### `POST /predict`



Accepts an image uploaded as multipart form data.



Example successful response:



```json

{

&#x20; "filename": "test.jpg",

&#x20; "total\_objects": 1,

&#x20; "detections": \[

&#x20;   {

&#x20;     "class": "bus",

&#x20;     "confidence": 0.9422,

&#x20;     "bounding\_box": \[

&#x20;       38.14,

&#x20;       11.39,

&#x20;       530.03,

&#x20;       335.21

&#x20;     ]

&#x20;   }

&#x20; ]

}

```



The example is illustrative of a previous test result; actual detections depend on the input image.



\## Testing



Run the image detection test from the project root:



```powershell

python backend/test\_yolo.py

```



The webcam script is available separately:



```powershell

python backend/webcam.py

```



The webcam script requires an accessible camera. The image-upload web interface does not require a webcam.



\## Future Improvements



\- Display bounding boxes directly on the uploaded image.

\- Add object-count summaries by class.

\- Support video-file detection through the web interface.

\- Add detection history and downloadable reports.

\- Improve inference performance and add evaluation metrics.

\- Deploy the application to a cloud platform.



\## Learning Outcomes



This project demonstrates practical experience with computer vision, pretrained object-detection models, image processing, REST API development, frontend-backend integration, and Python application development.



\## License



Choose and add an appropriate open-source license before distributing the project.



