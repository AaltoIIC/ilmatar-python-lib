import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

"""
Testing script for s-curve. Possibility to edit the parameters and view on graph.

"""

def generate_speed_profile(distance):

    print("Dist ", distance)

    # Distance parameters
    d_total = int(distance)  # Total distance to target in m
    dd = 1  # Distance step
    max_speed = min((d_total/4), 300) # mm/s?
    print("Max speed: ", max_speed)

    # S-curve parameters for acceleration and deceleration
    base_k = 1.3  # Steepness of the s-curve
    scale_k = max(1 / (d_total * 0.04), 0.0005)  # Scaling factor for k
    k = base_k * scale_k  # Adjusted steepness of the s-curve
    print("K factor: ", k)

    distances = np.array([100, 200, 300, 500, 1000, 2000, 3000, 4000])  # in mm
    d_acc_values = np.array([0.52, 0.65, 0.6, 0.44, 0.29, 0.2, 0.18, 0.17])  # d_acc values

    # Function to perform linear interpolation
    def get_d_acc(distance, distances, d_acc_values):
        return np.interp(distance, distances, d_acc_values)

    d_acc = int(d_total * get_d_acc(d_total, distances, d_acc_values))
    print("Acc length: ", d_acc)

    # Sigmoid function in distance domain
    def sigmoid(d, k, d_0):
        return 1 / (1 + np.exp(-k * (d - d_0)))

    # Derivative of the sigmoid function (speed profile)
    def sigmoid_derivative(d, k, d_0):
        s = sigmoid(d, k, d_0)
        return k * s * (1 - s)

    # Distance array
    d = np.arange(0, d_total, dd)
    speed_profile = np.zeros_like(d)

    # Acceleration phase
    accel_profile = sigmoid_derivative(d[:int(d_acc/dd)], k * 0.3, d_acc)
    speed_profile[:int(d_acc/dd)] = accel_profile / np.max(accel_profile) * max_speed

    # Constant speed phase
    speed_profile[int(d_acc/dd):int((d_total - d_acc)/dd)] = max_speed

    # Deceleration phase
    decel_profile = sigmoid_derivative(d[:int(d_acc/dd)], k, 0)
    speed_profile[int(((d_total - d_acc)/dd)):] = decel_profile / np.max(decel_profile) * max_speed

    remaining_distances = d_total - d  # Calculate remaining distances

    return speed_profile, remaining_distances


def s_curve(speed_profile, remaining_distances, distance):

    # Create interpolation function for speed based on remaining distance
    speed_interpolation = interp1d(remaining_distances, speed_profile, fill_value="extrapolate")

    def get_speed(remaining_distance):
        return speed_interpolation(remaining_distance)

    return float(get_speed(abs(distance)))


speeds = []
distances = np.arange(2000, 0, -1)
distance = distances[0]
speed_profile, remaining_distances = generate_speed_profile(distance)
for dist in distances:
    speed = s_curve(speed_profile, remaining_distances, dist)
    speeds.append(speed)
    #print(speed)

plt.plot(-distances, speeds)
plt.xlabel('Distance to target [mm]')
plt.ylabel('Velocity [units]')
plt.title('S-curve motion profile')
plt.show()