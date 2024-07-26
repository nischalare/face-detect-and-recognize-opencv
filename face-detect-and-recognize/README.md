# Face Detection and Recognition using OpenCV

## Description
A Python application using OpenCV to detect faces in real-time from a webcam feed.

## Project Structure
face-detect-and-recognize-opencv/
│
├── README.md
├── requirements.txt
├── haarcascade_frontalface_default.xml
└── src/
└── face_recognition.py

bash
Copy code

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/face-detect-and-recognize-opencv.git
cd face-detect-and-recognize-opencv
2. Set Up Virtual Environment (recommended)
bash
Copy code
# Create virtual environment (venv)
python -m venv face-detect-and-recognize-opencv

# Activate virtual environment
source face-detect-and-recognize-opencv/bin/activate   # for Linux/Mac
face-detect-and-recognize-opencv\Scripts\activate      # for Windows

# Install required libraries
pip install -r requirements.txt
3. Download Haar Cascade
Ensure you have the haarcascade_frontalface_default.xml file in the project directory. You can download it from OpenCV GitHub repository.

4. Install Dependencies
Ensure opencv-python and other required libraries are installed. If not installed globally, use the requirements.txt file:

bash
Copy code
pip install -r requirements.txt

cd face-detect-and-recognize
py src/face_recognition.py
