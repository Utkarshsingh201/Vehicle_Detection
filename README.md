Car Detection

A simple Python project that uses YOLOv11 and OpenCV to detect cars in a video.

Requirements
Python 3.8+
OpenCV
Ultralytics
Installation

Install the required packages:

pip install opencv-python ultralytics

Project Structure
project/
│
├── main.py
├── my_video.mp4
└── README.md

How to Use
1. Add your video

Put your video file in the same folder as main.py.

For example:

my_video.mp4

2. Set the video filename

Open main.py and change:

video_file = "my_video.mp4"


to your video filename.

For example:

video_file = "car_video.mp4"

3. Run the program

Open a terminal in the project folder and run:

python main.py


The program will open a window and detect cars in the video.

4. Stop the program

Press:

Q


to close the video.

YOLO Model

The project uses:

yolo11n.pt


This is the small and fast YOLOv11 model.

The model will be downloaded automatically by Ultralytics the first time you run the program.

Output

Detected cars will have:

A green bounding box
Confidence score

Example:

car 0.92


That's it! 🚗
