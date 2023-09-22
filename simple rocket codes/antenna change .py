import serial

# Configure the serial communication with the antenna controller
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Replace with your serial port and baud rate

def move_antenna(azimuth, elevation):
    command = f"MOVE {azimuth} {elevation}\n"
    ser.write(command.encode())

# Example usage:
try:
    target_azimuth = 180  # Example azimuth angle
    target_elevation = 30  # Example elevation angle
    move_antenna(target_azimuth, target_elevation)
except KeyboardInterrupt:
    pass

ser.close()
