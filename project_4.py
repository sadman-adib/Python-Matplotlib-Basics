import matplotlib.pyplot as plt
import numpy as np

a = np.arange(5) # x axis
b = [5,10,15,20,25] # y axis
c = [10,20,30,40,50] # y axis

fig = plt.figure()

axis = plt.subplot()

axis.plot(a, b, 'k--', label = 'line 1') # k-- = -----
axis.plot(a, c, 'k:', label = 'line 2') # k: = ........

lol = axis.legend(loc = 'lower right') # set the legend title in lower right
lol.get_frame().set_facecolor('aqua') # set legend title color

plt.title("2 different lines")

plt.show()