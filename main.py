
Controls 6 servo motors of a 5-DOF robotic arm using Bluetooth commands.
"""

import pigpio
import serial
import time

# ================== GPIO CONFIG ==================

SERVO_PINS = {
    "waist": 17,
    "shoulder": 18,
    "elbow": 19,
    "wrist_roll": 20,
    "wrist_pitch": 21,
    "gripper": 22,
}

# Servo pulse width range
MIN_PW = 500
MAX_PW = 2500

# ================== INIT ==================

print("🔌 Initializing pigpio...")
pi = pigpio.pi()

if not pi.connected:
    print("❌ Failed to connect to pigpio daemon.")
    exit()

print("✅ pigpio connected")

# Initialize Bluetooth serial
try:
    ser = serial.Serial("/dev/rfcomm0", 9600, timeout=1)
    print("📡 Bluetooth connected")
except Exception as e:
    print("❌ Bluetooth connection failed:", e)
    ser = None


# ================== FUNCTIONS ==================

def angle_to_pulse(angle):
    """Convert servo angle (0–180) to pulse width"""
    return int(MIN_PW + (angle / 180.0) * (MAX_PW - MIN_PW))


def move_servo(joint, angle):
    """Move specific servo joint"""
    if joint not in SERVO_PINS:
        print(f"⚠️ Unknown joint: {joint}")
        return

    pulse = angle_to_pulse(angle)
    pi.set_servo_pulsewidth(SERVO_PINS[joint], pulse)
    print(f"➡️ {joint} moved to {angle}°")


def parse_command(command):
    """
    Expected command format:
    joint:angle
    Example:
    waist:90
    """
    try:
        joint, angle = command.strip().split(":")
        angle = int(angle)
        move_servo(joint, angle)
    except Exception:
        print("⚠️ Invalid command:", command)


# ================== MAIN LOOP ==================

print("🚀 Robotic Arm Ready...")

try:
    while True:
        if ser and ser.in_waiting:
            data = ser.readline().decode().strip()
            if data:
                print("📥 Received:", data)
                parse_command(data)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\n🛑 Stopping robotic arm...")

finally:
    # Stop all servos
    for pin in SERVO_PINS.values():
        pi.set_servo_pulsewidth(pin, 0)

    if ser:
        ser.close()

    pi.stop()
    print("✅ Cleanup complete")
