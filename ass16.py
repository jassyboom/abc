import seaborn as sns
import matplotlib.pyplot as plt

# Load the inbuilt Titanic dataset
titanic = sns.load_dataset('titanic')

# Plot histogram of 'fare'
plt.figure(figsize=(10, 6))
plt.hist(titanic['fare'].dropna(), bins=30, edgecolor='black')
plt.title('Distribution of Passenger Fare')
plt.xlabel('Fare')
plt.ylabel('Number of Passengers')
plt.show()
