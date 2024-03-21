import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]  
φ = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]  

# Izračun srednje vrijednosti umnoška M i φ
mean_xy = np.mean(np.array(M) * np.array(φ))

# Izračun srednje vrijednosti kvadrata φ
mean_x_square = np.mean(np.array(φ)**2)

a = mean_xy / mean_x_square

mean_y_square = np.mean(np.array(M)**2)
deviation = math.sqrt(1 / len(M) * ((mean_y_square / mean_x_square) - a**2))

os_y = [a * x for x in φ]

plt.scatter(φ, M, color='green')
plt.plot(φ, os_y, color='red')
plt.xlabel('\u03A6 / [rad]')
plt.ylabel('M / Nm')
plt.show()
