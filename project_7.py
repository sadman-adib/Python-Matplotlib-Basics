import matplotlib.pyplot as plt

teamA = [10, 20, 40, 18, 15, 11]
teamB = [20, 80, 45, 30, 29, 28]

score_range = [5, 10, 15, 20, 25, 30]

plt.scatter(teamA, score_range, color = 'red')
plt.plot(teamA, score_range, color = 'black')
plt.scatter(teamB, score_range, color = 'blue')
plt.plot(teamB, score_range, color = 'black')

plt.xlabel("team score")
plt.ylabel("score range")

plt.title("score range of match")

plt.show()