import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
 
data = pd.read_csv(url)
# display the first 5 rows of the dataset
# print(data.head(5))

# display the first 10 rows of the dataset
print(data.head(10))

print(data.shape)
print(data.columns)
data.info()
print(data.describe())

# Count the number of flowers belonging to each species:
print(data["species"].value_counts())

# Create a bar plot showing the number of flowers belonging to each species
data["species"].value_counts().plot(kind="bar")

plt.title("Number of Flowers by Species")
plt.xlabel("Species")
plt.ylabel("Number of Flowers")

plt.show()