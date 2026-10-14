from ultralytics import YOLO


# Load YOLO model once
model = YOLO("yolo11n.pt")


def detect_objects(image):
    """
    Run YOLO object detection on an image.
    """

    results = model(image)

    result = results[0]

    detections = []

    for box in result.boxes:

        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        class_name = result.names[class_id]

        bounding_box = box.xyxy[0].tolist()

        detections.append({
            "class": class_name,
            "confidence": round(confidence, 4),
            "bounding_box": bounding_box
        })

    return detections