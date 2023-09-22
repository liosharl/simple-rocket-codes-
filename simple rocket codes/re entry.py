class Rocket:
    def __init__(self):
        self.position = "In space"
        self.password = "secure123"  # change to Set your secure password here

    def return_to_earth(self, password):
        if password == self.password:
            self.position = "Returning to Earth"
            print("Rocket is now returning to Earth.")
            
        else:
            print("Accces Denid!!!,Unauthorized access.The Correct Password is required to initiate the return.")

def main():
    rocket = Rocket()

    while True:
        command = input("Enter command ('return' to initiate return, 'quit' to exit): ")

        if command.lower() == 'return':
            password = input("Enter password to initiate return: ")
            rocket.return_to_earth(password)
        elif command.lower() == 'quit':
            break
        else:
            print("Invalid command. Try 'return' or 'quit'.")

if __name__ == "__main__":
    main()
