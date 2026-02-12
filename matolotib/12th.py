import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]

NOP1 = [5, 4, 3, 6, 7, 4, 5]
NOP2 = [2, 5, 6, 9, 4, 6, 3]
NOP3 = [3, 4, 9, 2, 5, 3, 4]

plt.stackplot(days, NOP1, NOP2, NOP3)
plt.xlabel("Days")
plt.ylabel("Number of People")
plt.title("Stack Plot Example")
plt.show()
