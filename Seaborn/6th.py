import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (correct name)
data = sns.load_dataset("exercise")

# Bar plot (correct syntax)
sns.barplot(x="day", y="pulse", data=data)

plt.show()
