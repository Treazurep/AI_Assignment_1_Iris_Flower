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

# Create a histogram showing the distribution of petal length
plt.hist(data["petal_length"])
 
plt.title("Distribution of Petal Length")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
 
plt.show()

# Create a scatter plot comparing: Petal Length vs. Petal Width
sns.scatterplot(
    data=data,
    x="petal_length",
    y="petal_width",
    hue="species"
)
 
plt.title("Petal Length vs. Petal Width")
 
plt.show()

# Create my own scatter plot comparing: Sepal Length vs. Sepal Width
sns.scatterplot(
    data=data,
    x="sepal_length",
    y="sepal_width",
    hue="species"
)

plt.title("Sepal Length vs. Sepal Width")

plt.show()