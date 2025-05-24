import serial
import time

def caesar_decrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

print("Waiting for message...")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        print("Encrypted message received:", line)
        print("Decrypted message:", caesar_decrypt(line, 3))
        break
