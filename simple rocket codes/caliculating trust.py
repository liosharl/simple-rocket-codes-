def calculate_thrust(rocket_mass, desired_acceleration, gravitational_force):
    # Calculate thrust needed to achieve desired acceleration
    thrust = rocket_mass * (desired_acceleration + gravitational_force)
    return thrust

# Constants
rocket_mass = 1000  #Change the Mass of the rocket in kilograms
desired_acceleration = 100000  # change to the Desired acceleration in meters per second squared
gravitational_force_earth = 9.81  # Gravitational force on Earth in meters per second squared

# Calculate thrust
required_thrust = calculate_thrust(rocket_mass, desired_acceleration, gravitational_force_earth)

print(f"Required thrust: {required_thrust} Newtons")



#rocket_mass is the mass of the rocket in kilograms.
#desired_acceleration is the desired acceleration, typically expressed in meters per second squared (m/s^2).
#gravitational_force_earth is the gravitational force on Earth, approximately 9.81 m/s^2.
#The calculate_thrust function calculates the thrust required to achieve the desired acceleration, taking into account the gravitational force acting on the rocket.