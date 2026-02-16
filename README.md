# 🤖 Robotic Arm Using Raspberry Pi

## 📌 Overview
This project implements a 5-DOF robotic arm controlled using Raspberry Pi and Python. The system enables precise pick-and-place operations using six servo motors and an Android application built with MIT App Inventor. The robotic arm supports smooth, low-jitter motion control and real-time manual as well as automated movement playback.

## 🚀 Key Features
- 5 DOF robotic arm with gripper control  
- Raspberry Pi–based servo control using Python  
- Android app control via Bluetooth (SPP)  
- Zero-jitter smooth servo movement  
- Motion recording and replay functionality  
- Single 5V power supply operation  

## 🛠️ Hardware Components
- Raspberry Pi 3  
- MG995 Servo Motors (3)  
- SG90 Servo Motors (3)  
- 5V 2.5A Power Supply  
- Jumper wires and mounting hardware  
- 3D printed robotic arm structure  

## 💻 Software Stack
- Python 3  
- pigpio library  
- Raspberry Pi OS  
- MIT App Inventor (Android control app)  
- Bluetooth SPP communication  

## ⚙️ System Architecture
1. Android app sends commands via Bluetooth.  
2. Raspberry Pi receives serial data.  
3. Python script processes movement commands.  
4. pigpio controls servo PWM signals.  
5. Robotic arm executes motion.

## 🔌 GPIO Servo Mapping
| Joint | Servo Type | GPIO |
|------|-----------|------|
| Waist | MG995 | GPIO 17 |
| Shoulder | MG995 | GPIO 18 |
| Elbow | MG995 | GPIO 19 |
| Wrist Roll | SG90 | GPIO 20 |
| Wrist Pitch | SG90 | GPIO 21 |
| Gripper | SG90 | GPIO 22 |

*(Based on wiring diagram from project)*

## 📸 Demo
![Robotic Arm](assets/demo.png)

## ▶️ How to Run

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade

# Enable pigpio
sudo systemctl enable pigpiod
sudo systemctl start pigpiod

# Run project
python3 robarm.py
