# Smart Surveillance AI

An intelligent real-time surveillance system powered by Artificial Intelligence and Computer Vision.

This project combines facial recognition, motion detection, person tracking and intelligent monitoring to create a smart surveillance platform capable of analyzing live video streams in real time.

---

# Project Vision

Traditional surveillance systems only record video footage.

Smart Surveillance AI goes further by introducing artificial intelligence capabilities that allow the system to:

- Detect human presence automatically
- Recognize known individuals
- Identify unknown persons
- Monitor suspicious movement
- Generate surveillance logs
- Send intelligent alerts

The goal of this project is to build an intelligent surveillance assistant capable of understanding and analyzing live video activity instead of simply recording it.

---

# Why This Project Matters

Modern security systems increasingly rely on Artificial Intelligence for:

- Smart cities
- Intelligent buildings
- Access control systems
- Industrial monitoring
- Automated security
- Real-time threat detection

This project is designed as both:

- a practical AI engineering project
- a research-oriented computer vision platform

that can evolve into advanced intelligent surveillance research.

---

# Main Features

## Real-Time Face Recognition

The system can recognize registered individuals using facial recognition algorithms.

When a known face is detected:
- the identity is displayed
- confidence score is calculated
- access events can be logged

Unknown individuals are automatically labeled as unknown.

---

## Motion Detection

The platform continuously analyzes camera activity to detect movement inside the monitored area.

This helps reduce unnecessary processing and improves surveillance efficiency.

---

## Person Detection

The system can identify human presence inside the video stream in real time.

This allows future integration of:
- human tracking
- crowd analysis
- behavior analysis
- anomaly detection

---

## Intelligent Logging System

Surveillance events are automatically stored in logs, including:
- timestamps
- detection events
- recognition events
- alerts

This provides traceability and monitoring history.

---

## Email Alert Service

The platform includes an alert system capable of sending notifications when suspicious activity or unknown persons are detected.

---

# System Workflow

The surveillance pipeline follows several stages:

```text
Camera Stream
      ↓
Motion Detection
      ↓
Person Detection
      ↓
Face Detection
      ↓
Face Recognition
      ↓
Event Logging
      ↓
Alert System
```

Each module works independently in a modular architecture, making the platform scalable and extensible.

---

# Technologies Used

This project combines several AI and software engineering technologies:

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Real-time video processing |
| face_recognition | Facial recognition |
| Dlib | Face embeddings and detection |
| TensorFlow | AI / Deep Learning support |
| NumPy | Numerical processing |

---

# Project Structure

```text
smart-surveillance-ai/
│
├── src/
│   ├── modules/
│   │   ├── face_detector.py
│   │   ├── face_recognizer.py
│   │   ├── motion_detector.py
│   │   └── person_detector.py
│   │
│   ├── services/
│   │   ├── email_service.py
│   │   └── logger_service.py
│   │
│   ├── utils/
│   └── main.py
│
├── models/
├── logs/
├── data/
└── README.md
```

---

# Current Status

Current implemented capabilities:

- Real-time surveillance
- Face recognition
- Motion detection
- Person detection
- Logging system
- Email alerts
- Modular architecture

---

# Future Improvements

The project is actively evolving toward a more advanced AI surveillance platform.

Planned future improvements include:

- YOLOv8 integration
- DeepSORT object tracking
- Multi-camera support
- PostgreSQL database
- FastAPI web dashboard
- Docker deployment
- Grafana monitoring
- Behavioral analysis
- Intrusion detection
- Edge AI optimization

---

# Research Perspective

This project is also intended for experimentation and research in:

- Computer Vision
- Intelligent Surveillance Systems
- Real-Time Video Analytics
- Deep Learning
- Smart Security Systems
- AI-powered Monitoring Platforms

The long-term objective is to transform this platform into a scalable intelligent surveillance ecosystem suitable for research and industrial applications.

---

# Screenshots

Real-time facial recognition and tracking interface:

(Add screenshots here)

---

# Author

Edouard Junior Mobeko

Master's Student in Computer Science  
Artificial Intelligence • Computer Vision • Smart Systems • DevOps

---

# License

MIT License