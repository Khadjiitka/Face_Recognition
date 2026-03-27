# Real-Time Face Detection
This is a lightweight Python application that uses the **Haar Cascade** algorithm to detect human faces in real-time via a webcam feed. It is a perfect starting point for computer vision enthusiasts.

## 📌 Overview

This project utilizes the `OpenCV` library to capture video frames, convert them to grayscale for processing, and apply a pre-trained classifier to identify facial features. Once a face is detected, the program draws a bounding box around it.

<br> ![image](https://github.com/Khadjiitka/Face_Recognition/blob/f1b48b754ebe626939e29bd186a51787693a5a36/example.jpg)

## 🚀 Features

* **Real-time Processing:** Fast detection directly from your webcam.
* **Grayscale Optimization:** Converts frames to grayscale to reduce computational load.
* **Visual Feedback:** Draws red rectangles around detected faces.
* **Simple Exit:** Press the `q` key to stop the script instantly.

## 🔍 Technical Details
The script follows a simple 4-step pipeline:
* **Capture:** Reads frames from the default camera using *cv2.VideoCapture(0)*.
* **Pre-process:** Converts frames to grayscale to simplify the mathematical detection.
* **Detect:** Uses the *detectMultiScale method*. The sensitivity is controlled by:*scaleFactor*: How much the image size is reduced at each image *scale.minNeighbors*: How many neighbors each candidate rectangle should have to retain it.
* **Display:** Draws a rectangle using the coordinates $(x, y)$ and dimensions $(w, h)$ found by the classifier.

<br>

  >**Tip:** If you experience "ghost" faces (false positives), try increasing the minNeighbors value in the code.
