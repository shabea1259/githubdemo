import serial
import time

PORT = 'COM5'       # Change to your Arduino's COM port
BAUD = 9600
TIMEOUT = 2

def main():
    print("Opening serial connection...")
    ser = serial.Serial(PORT, BAUD, timeout=TIMEOUT)

    time.sleep(2)   # Wait for Arduino to reset

    print("Connected to Arduino")

    # Send message
    ser.write(b'hi\n')
    print("Sent: hi")

    # Wait for reply
    print("Waiting for reply...")
    reply = ser.readline().decode('utf-8').strip()

    if reply:
        print("Arduino replied:", reply)
    else:
        print("No reply (timeout)")

    ser.close()

if __name__ == '__main__':
    main()
