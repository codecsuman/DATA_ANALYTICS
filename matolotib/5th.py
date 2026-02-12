import numpy as np
import matplotlib.pyplot as plt


x = np.random.randint(1,10,50)
y = np.random.randint(10,100,50)

plt.scatter(x,y, marker ="*", color="red")
plt.show()