import matplotlib.pyplot as plt 
import numpy as np 

# Generate 'x' and 'y' data
N = 500
x = np.random.uniform(0.0, 1.0, N)
y = np.random.uniform(0.0, 1.0, N)

# Configure the scatter plot
plt.scatter(x, y)
plt.title("Exercise #2 Scatter Plot")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
