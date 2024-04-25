import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
file_path = 'IT_Salary_Survey.csv'
df = pd.read_csv(file_path)
# selected_columns = df[['Total years of experience', 'Years of experience in Germany']]
selected_columns = df[['Total years of experience', 'Years of experience in Germany']]

print(selected_columns)

# Convert the 'Total years of experience' column to numeric values
def calculate_experience(age):
    years = [int(i) for i in str(age).split('-')]
    if len(years) == 2:
        return np.mean(range(years[0], years[1] + 1))
    else:
        return np.nan

df['Age'] = df['Age'].apply(calculate_experience)
# Calculate mean, median, mode
mean_value = df['Total years of experience'].mean()
median_value = df['Total years of experience'].median()
mode_value = df['Total years of experience'].mode().iloc[0]

# Calculate range
range_value = df['Total years of experience'].max() - df['Years of experience in Germany'].min()

# Calculate variation and standard deviation
variation_value = df['Total years of experience'].var()
std_dev_value = df['Total years of experience'].std()

skewness_value = df['Total years of experience'].skew()

# Display the results
print(f'Mean: {mean_value}')
print(f'Median: {median_value}')
print(f'Mode: {mode_value}')
print(f'Range: {range_value}')
print(f'Variation: {variation_value}')
print(f'Standard Deviation: {std_dev_value}')
print(f'Skewness: {skewness_value}')