import time

def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"Time remaining: {i} seconds", end='\r')
        time.sleep(1)
    print("Countdown complete! launch")

# Set the countdown duration in seconds
countdown_duration = 100

countdown(countdown_duration)
