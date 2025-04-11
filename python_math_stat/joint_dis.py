import matplotlib.pyplot as plt
import numpy as np

# Define the vertices of the diamond region.
# For |x|+|y| = 1, the vertices are (1,0), (0,1), (-1,0), and (0,-1).
x_diamond = [1, 0, -1, 0, 1]
y_diamond = [0, 1, 0, -1, 0]

# Create the figure and axis.
fig, ax = plt.subplots(figsize=(6,6))

# Plot the boundary of the diamond.
ax.plot(x_diamond, y_diamond, 'b-', lw=2, label='Support Boundary: |x| + |y| = 1')

# Fill the diamond area with a light color.
ax.fill(x_diamond, y_diamond, color='skyblue', alpha=0.3)

# Label the axes and set equal aspect ratio.
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Diamond Support Region: |x| + |y| ≤ 1')

# Mark a point (0.9, 0.9) which is not inside the diamond.
ax.plot(0.9, 0.9, 'ro', label='Point (0.9,0.9) with fXY=0')
ax.annotate('(0.9,0.9)', (0.9, 0.9), xytext=(0.8, 1.0),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3'))

# Illustrate the constraint if we fix x=0.9:
# For a fixed x = 0.9, the diamond inequality |0.9|+|y| ≤ 1 implies |y| ≤ 0.1.
# Thus, y can only be in the interval [-0.1, 0.1].
ax.vlines(0.9, -0.1, 0.1, colors='r', linestyles='--', label='Allowed y for x=0.9: |y| ≤ 0.1')

# Add grid and legend.
ax.grid(True)
ax.legend()

plt.show()