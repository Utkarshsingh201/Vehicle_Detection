## Car Detection

A simple car detection system using YOLOv11 and OpenCV.

The program reads a video, detects cars, and draws a bounding box around each detected car.

Make sure you have:

Python 3.8 or newer
OpenCV
Ultralytics
Install Dependencies

Open your terminal and run:

pip install opencv-python ultralytics

📁 Project Structure

Your project should look like this:

YOLO-Car-Detection/
│
├── main.py
├── my_video.mp4
└── README.md


You can use any video file. Just make sure the filename matches the one in main.py.

### ▶️ How to Run
1. Add your video

Place your video inside the project folder.

For example:

my_video.mp4

### 2. Set the video name

Open main.py and find:

video_file = "my_video.mp4"


Change it if your video has a different name:

video_file = "car_video.mp4"

### 3. Run the program

Open a terminal inside the project folder:

python main.py


The video will open in a new window and cars will be detected automatically.

### ⏹️ Stop the Program

While the video window is open, press:

Q


to stop the program.


