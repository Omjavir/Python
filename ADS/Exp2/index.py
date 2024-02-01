import pandas as pd
from statistics import variance
from statistics import stdev

data = pd.read_csv(r"Space_Missions.csv")[['Timestamp','Age','Gender','Total years of experience','Seniority level','Сontract duration']]
# df = pd.DataFrame(data)

# mean meadian mode

print("Mean of the   Dataset")
print(data.mean())
print("\n**")
print("Median of the  Dataset")
print(data.median())
print("\n**")
print("Mode of the  Dataset")
print(data.mode())

print("\n**")


# range
print("Range: ")
range1 = data['Timestamp'].max() - data['Age'].min()
range2 = data['Gender'].max() - data['Total years of experience'].min()
print("Range of Timestamp: " + str(range1))
print("Range of Gender : " + str(range2))

print("\n**")

# variance
print("Variance: ")
variance1 = variance(data['Timestamp'])
variance2 = variance(data['Gender'])
print("Variance of Timestamp': " + str(variance1))
print("Variance of Gender: " + str(variance2))

print("\n**")

# standard deviation
print("Standard Deviation: ")
std1 = stdev(data['Timestamp'])
std2 = stdev(data['Gender'])
print("Standard Deviation of Timestamp:" + str(std1))
print("Standard Deviation of Gender: " + str(std2))

print("\n**")

print('\Skewness of Dataset')
#skewness
# print('Skewness')
skew1 = data['Timestamp'].skew()
skew2 = data['Gender'].skew()
print("Skewness of Timestamp: " + str(skew1))
print("Skewness of Gender: " + str(skew2))