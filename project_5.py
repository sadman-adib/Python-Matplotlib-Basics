import matplotlib.pyplot as plt
import numpy as np

month = np.array(["january", "february", "march", "april", "december"])
temperature = np.array([28, 31, 40, 41, 25])

plt.plot(month, temperature)

plt.xlabel("month name")
plt.ylabel("temperature level in degree(c)")

plt.title("temperature level of year 2023")

plt.show()