import matplotlib.pyplot as plt
import numpy as np

marks = [1, 2, 5, 10, 20, 25, 26, 27, 30, 40, 50, 55, 65, 66, 67, 68, 70, 75, 90]

plt.hist(marks, bins=[0, 20, 40, 60, 80, 100])

plt.xlabel("marks")
plt.ylabel("frequency of students")

plt.title("students result marks")

plt.show() # printing a histogram