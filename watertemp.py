import matplotlib.pyplot as plt
import numpy as np

# Data input in bar
x = np.array(["03/20", "03/21", "03/22", "03/23", "03/24", "03/25", "03/26"])
y = np.array([21, 21, 21, 19, 19, 21, 21])

# Label 1
plt.title("Water temperature in Okinawa March 2024")
plt.ylabel("Water temperature (C)")
plt.xlabel("Time period")

# Data output in bar
plt.bar(x,y)
plt.show()

# Data input in line
xpoints = np.array(["03/20", "03/21", "03/22", "03/23", "03/24", "03/25", "03/26"])
ypoints = np.array([21, 21, 21, 19, 19, 21, 21])

# Label
plt.title("Water temperature in Okinawa March 2024")
plt.ylabel("Water temperature (C)")
plt.xlabel("Time period")

# Data output in in
plt.plot(xpoints, ypoints)
plt.show()
