import numpy as np
import matplotlib.pyplot as plt

# Constants
initial_altitude = 0  # Initial altitude in meters
initial_speed = 0  # Initial speed in m/s
initial_angle = 0  # Initial launch angle in degrees
gravity = 9.81  # Acceleration due to gravity in m/s^2
thrust_angle = 15  # Angle at which to tilt the rocket at 30,000 km altitude
altitude_target = 30000 * 1000  # Target altitude in meters

# Time step and simulation parameters
dt = 0.1  # Time step in seconds
time = 0  # Initial time
altitude = initial_altitude
speed = initial_speed
angle = initial_angle

# Lists to store simulation data
altitudes = []
speeds = []

# Simulation loop
while altitude < altitude_target:
    # Calculate thrust and update rocket parameters
    # Here, you would need to implement more sophisticated calculations for thrust and control
    thrust = 0  # Replace with a function that calculates thrust based on rocket design
    
    # Update rocket dynamics
    acceleration = thrust / mass - gravity
    speed += acceleration * dt
    altitude += speed * dt
    angle = thrust_angle if altitude >= altitude_target else initial_angle
    
    # Store simulation data
    altitudes.append(altitude)
    speeds.append(speed)
    
    # Update time
    time += dt

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(np.arange(0, time, dt), altitudes)
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Rocket Altitude vs. Time')
plt.grid(True)
plt.show()
