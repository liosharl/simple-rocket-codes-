import time

class RocketCamera:
    def __init__(self):
        self.picture_count = 0

    def take_picture(self):
        self.picture_count += 1
        print(f"Picture taken! Picture {self.picture_count} captured.")

def main():
    rocket_camera = RocketCamera()
    
    while True:
        command = input("Enter 'take picture' to capture a picture (or 'quit' to exit): ")
        
        if command.lower() == 'take picture':
            rocket_camera.take_picture()
        elif command.lower() == 'quit':
            break
        else:
            print("Invalid command. Try 'take picture' or 'quit'.")

if __name__ == "__main__":
    main()
