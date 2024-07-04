import matplotlib.pyplot as plt
import pandas as pd

data = {
    "name" : ["Sadman", "Nabila", "Atoshe"],
    "age" : [21, 22, 23],
    "cgpa" : [3.5, 3.9, 3.7]
}

dataframe = pd.DataFrame(data)

plt.xlabel("age")
plt.ylabel("cgpa")

plt.plot(dataframe["age"], dataframe["cgpa"])
plt.grid()
plt.title("age & cgpa of students")

plt.show()
