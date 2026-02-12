import matplotlib.pyplot as plt

x = ["day1", "day2", "day3", "day4"]
y = [300, 400, 260, 800]

# Line 1
plt.plot(x, y, marker="^", ls="--", color="red", label="Triangle Line")

# Line 2
plt.plot(x, y, marker="o", label="Circle Line")

plt.xlabel("Days")
plt.ylabel("Values")
plt.title("Daily Data")
plt.legend()

plt.show()
 