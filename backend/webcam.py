import cv2
import time
from ultralytics import YOLO


# --------------------------------
# 1. Load YOLO model
# --------------------------------
model = YOLO("yolo11n.pt")


# --------------------------------
# 2. Open webcam
# --------------------------------
cap = cv2.VideoCapture(0)


# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()


# --------------------------------
# 3. FPS variables
# --------------------------------
prev_time = 0


# --------------------------------
# 4. Real-time detection loop
# --------------------------------
while True:

    # Read frame from webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break


    # --------------------------------
    # 5. Run YOLO detection
    # --------------------------------
    results = model(frame)


    # Draw bounding boxes and labels
    annotated_frame = results[0].plot()


    # --------------------------------
    # 6. Calculate FPS
    # --------------------------------
    current_time = time.time()

    if prev_time != 0:
        fps = 1 / (current_time - prev_time)
    else:
        fps = 0

    prev_time = current_time


    # --------------------------------
    # 7. Display FPS
    # --------------------------------
    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )


    # --------------------------------
    # 8. Display webcam
    # --------------------------------
    cv2.imshow(
        "Real-Time Object Detection",
        annotated_frame
    )


    # --------------------------------
    # 9. Press Q to quit
    # --------------------------------
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# --------------------------------
# 10. Release resources
# --------------------------------
cap.release()
cv2.destroyAllWindows()

print("Webcam detection stopped.")