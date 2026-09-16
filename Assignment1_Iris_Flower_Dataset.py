import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
 
data = pd.read_csv(url)

# display the first 5 rows of the dataset
print(data.head(5))