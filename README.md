# AI-Based Intelligent Camera Security System

# Project Overview

This project is an AI-based intelligent surveillance system developed using Python, YOLOv8, and OpenCV. The system detects suspicious weapons in real-time video/webcam streams and generates alerts for security monitoring applications.



This project demonstrates a prototype intelligent surveillance pipeline for real-time weapon detection using deep learning and computer vision techniques.


# Features

- Real-time weapon detection
- Webcam and video input support
- Bounding box visualization
- Confidence score display
- Screenshot saving
- Modular project structure

# Dataset

Weapon detection dataset collected from Kaggle public datasets. Dataset was cleaned and converted into a single-class weapon detection format for surveillance-oriented detection.

# Model Used

YOLOv8 Nano model was used for transfer learning and fine-tuned on the custom weapon detection dataset.

# System Architecture


The intelligent surveillance system follows the below pipeline:

Video/Webcam Input
        ↓
Frame Capture using OpenCV
        ↓
YOLOv8 Weapon Detection
        ↓
Bounding Box & Confidence Extraction
        ↓
Alert Generation
        ↓
Visualization & Result Display
        ↓
Screenshot / Output Saving

Components Used:
- OpenCV for video processing
- YOLOv8 for real-time weapon detection
- Python for inference pipeline
- Custom-trained weapon detection model


# Installation

pip install -r requirements.txt

# Training

python train_weapon_model.py

# Inference

python main.py

# Results

The model successfully detects weapons in webcam/video streams with real-time visualization and alert capability.

# Evaluation Metrics

Add approximate metrics from training:

   *) Precision - 
   *) Recall    -
   *) mAP50     - 


# Limitations

- Limited dataset diversity
- Performance may reduce in low-light conditions
- False positives possible for toy weapons or unclear objects

# Future Improvements

- DeepSORT-based object tracking
- Multi-person surveillance
- Real-time notification system
- Cloud logging and analytics
