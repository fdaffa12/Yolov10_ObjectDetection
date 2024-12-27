import cv2
import math
import cvzone
from ultralytics import YOLO
from tkinter import filedialog
import tkinter as tk

# Create tkinter window and hide it
root = tk.Tk()
root.withdraw()

# Open file dialog to select video
video_path = filedialog.askopenfilename(
    title="Pilih Video",
    filetypes=[
        ("Video files", "*.mp4 *.avi *.mov *.mkv"),
        ("All files", "*.*")
    ]
)

if not video_path:
    print("Tidak ada video yang dipilih.")
    exit()

# Initialize video capture
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Initialize video writer
output_path = 'output_detection.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (960, 540))  # Adjusted to match resize dimensions

# Load YOLO model with custom weights
model = YOLO("Weights/best.pt")

# Define class names and colors (BGR format)
classNames = ['With Helmet', 'Without Helmet']
colors = [(0, 255, 0), (0, 0, 255)]  # Green for with helmet, Red for without helmet

while True:
    success, img = cap.read()
    if not success:
        print("End of video or cannot read frame.")
        break

    # Perform object detection
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            # Draw bounding box and label if confidence > 0.5
            if conf > 0.5:
                # Use different colors based on class
                color = colors[cls]
                cvzone.cornerRect(img, (x1, y1, w, h), colorC=color)
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', 
                                 (max(0, x1), max(35, y1)), 
                                 scale=1, thickness=1,
                                 colorR=color,
                                 colorT=(255,255,255))  # White text

    # Resize image
    img = cv2.resize(img, (960, 540))
    
    # Write frame to output video
    out.write(img)
    
    # Display frame
    cv2.imshow("Helmet Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()