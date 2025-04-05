import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter for the distribution
lambda_value = 1.0  # You can adjust this value

# Define the grid for x and y
x = np.linspace(0, 10, 200)
y = np.linspace(0, 10, 200)
X, Y = np.meshgrid(x, y)

# Define the joint density function
F = np.where(X <= Y, lambda_value**2 * np.exp(-lambda_value * Y), 0)

# 3D Surface Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X, Y, F, cmap='viridis', edgecolor='none')
ax.set_title("Joint Density f(x,y)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x,y)")
fig.colorbar(surface, shrink=0.5, aspect=5, label="f(x,y)")
plt.show()

# Contour Plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, F, levels=50, cmap='viridis')
plt.title("Contour Plot of Joint Density f(x,y)")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(contour, label="f(x,y)")
plt.show()