import cv2
import time
from ultralytics import YOLO

def main(video_path):
    # Load YOLOv11 model
    model = YOLO("yolo11n.pt")  # small, fast version

    # Open your video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f" Error: Cannot open video file {video_path}")
        return

    # Get the video's frames per second (FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30  # fallback in case FPS isn't detected
    frame_delay = 1 / fps  # seconds between frames

    # Desired display width and height (adjust to fit your screen)
    display_width = 1400
    display_height = 700

    print(f"🎥 Processing video at {fps:.2f} FPS...")

    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            print(" Video processing completed.")
            break

        # Run YOLOv11 detection
        results = model(frame)

        # Filter detections: only cars
        filtered_boxes = []
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            if class_name == "car":
                filtered_boxes.append(box)

        # Draw boxes only for cars
        annotated_frame = frame.copy()
        for box in filtered_boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            label = f"car {conf:.2f}"

            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(annotated_frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Resize the frame for display
        resized_frame = cv2.resize(annotated_frame, (display_width, display_height))

        # Show the frame
        cv2.imshow("YOLOv11 - Car Detection", resized_frame)

        # Calculate time to match original FPS
        # elapsed = time.time() - start_time
        # sleep_time = max(0, frame_delay - elapsed)
        # time.sleep(sleep_time)

        # Quit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # 👇 Replace this with your actual video path
    video_file = "my_video.mp4"
    main(video_file)
