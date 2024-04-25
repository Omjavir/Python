import pandas as pd
import numpy as np
from tabulate import tabulate
from scipy.stats import skew

df = pd.read_csv('IT_Salary_Survey.csv')
df.head()
df.fillna(0, inplace=True)

data = [
    ['Mean', df['Age'].mean()],
    ['Median', df['Age'].median()],
    ['Mode', df['Age'].mode()[0]],
    ['Standard Deviation', df['Age'].std()],
    ['Range', df['Age'].max() - df['Age'].min()],
    ['Variance', df['Age'].var()],
    ['Skewness', skew(df['Age'])],
]
print("Age:")
print(tabulate(data, headers=['Metric', 'Value'], tablefmt='fancy_grid'))