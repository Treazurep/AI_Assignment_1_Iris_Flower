import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
 
data = pd.read_csv(url)
# display the first 5 rows of the dataset
# print(data.head(5))

# display the first 10 rows of the dataset
print(data.head(10))

data.shape
data.columns
data.info()
data.describe()