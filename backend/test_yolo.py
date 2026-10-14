from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolo11n.pt")

# Run detection
results = model("data/images/test.jpg")

# Get the first result
result = results[0]

# Print detected objects
for box in result.boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])

    class_name = result.names[class_id]

    coordinates = box.xyxy[0].tolist()

    print("Object:", class_name)
    print("Confidence:", round(confidence, 2))
    print("Bounding Box:", coordinates)
    print("-------------------------")

# Save detected image
result.save(filename="outputs/detected.jpg")

print("Detection completed!")
print("Result saved to outputs/detected.jpg")