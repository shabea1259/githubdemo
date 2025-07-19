import serial
import time

# Connect to Arduino COM5
arduino = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for Arduino to reset

arduino.write(b"TURN ON LIGHT\n")
print("[Python] Sent: TURN ON LIGHT")

while True:
    if arduino.in_waiting > 0:
        response = arduino.readline().decode().strip()
        print(f"[Arduino] {response}")

        if "Should I turn OFF the light?" in response:
            user_input = input("Arduino asks: Should I turn OFF the light? (yes/no): ").strip().lower()
            if user_input == "yes":
                arduino.write(b"yes\n")
                time.sleep(1)
                print("Stopped running this script.")
                break
            else:
                arduino.write(b"no\n")
                time.sleep(1)
                print("Waiting for your comment.")

