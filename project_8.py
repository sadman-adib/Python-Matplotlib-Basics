import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1) # 0,1,2,3,....9
y = abs(x) # absolute value of x
z = x**(1/2) # root x
# a = x**2 # x^2
# b = x**3 # x^3

plt.plot(x, y, color = "violet")
plt.plot(x, z, color = "violet")
# plt.plot(x, a, color = "violet")
# plt.plot(x, b, color = "violet")
plt.scatter(x, y, color='green', s=100, marker='*') # s is marker size
plt.scatter(x, z, color='blue', s=100, marker='*') # s is marker size
# plt.scatter(x, a, color='red', s=100, marker='*') # s is marker size
# plt.scatter(x, b, color='black', s=100, marker='*') # s is marker size
plt.show()