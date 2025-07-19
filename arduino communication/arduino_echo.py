import serial
import time

PORT = 'COM5'  # 🔁 Change this to your port if needed
BAUD = 9600
TIMEOUT = 2

def main():
    ser = serial.Serial(PORT, BAUD, timeout=TIMEOUT)
    time.sleep(2)  # Give Arduino time to reset
    print("Connected to Arduino!")

    while True:
        msg = input("Enter message (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break

        ser.write((msg + '\n').encode())
        print("Sent:", msg)

        reply = ser.readline().decode('utf-8').strip()
        print("Arduino replied:", reply)

    ser.close()
    print("Disconnected.")

if __name__ == '__main__':
    main()
