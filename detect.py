from ultralytics import YOLO
import cv2
import os

# Load model (place your trained YOLOv8 model in model/ folder)
MODEL_PATH = "model/defects.pt"

def run_detection(image_path, conf_threshold=0.4):
    if not os.path.exists(MODEL_PATH):
        return image_path, []  # fallback if model not loaded

    model = YOLO(MODEL_PATH)
    results = model.predict(source=image_path, conf=conf_threshold, save=False, verbose=False)

    image = cv2.imread(image_path)
    detections = []

    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            detections.append({
                "label": label,
                "confidence": conf,
                "box": (x1, y1, x2, y2)
            })

            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(image, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    output_path = os.path.splitext(image_path)[0] + "_output.jpg"
    cv2.imwrite(output_path, image)

    return output_path, detections

