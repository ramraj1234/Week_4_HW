import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT, MEDV = np.loadtxt("/Users/ramrajvemuri/Downloads/Data Science Bootcamp Resources/boston_housing_data.csv",skiprows=1, unpack=True, delimiter =',')

# Q1
width = 12
height = 8
style_name = "dark_background"
plt.style.use(style_name)
x = np.arange(0,len(ZN))
fig1, ax1 = plt.subplots()
ax1.plot(x, ZN, color="green", linestyle="-")
ax1.plot(x, INDUS, color="blue", linestyle="--")
plt.show()

#Q2
positive_range = 10
data1 = np.random.rand(10, 2) * positive_range
df = pd.DataFrame(data1, 
                  columns=['col1', 'col2'],
                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
bar_width = 0.4
x = np.arange(len(df))
plt.bar(x, df['col1'], width=bar_width, label='col1', align='center', alpha=0.7)
x2 = x + bar_width
plt.bar(x2, df['col2'], width=bar_width, label='col2', align='center', alpha=0.7)
plt.xticks(x + bar_width / 2, df.index)
plt.title('col1 and col2 data')
plt.legend(loc='lower left')
plt.show()
y = np.arange(len(df))
bar_height = 0.4
plt.barh(y, df['col1'], height=bar_height, label='col1', align='center', alpha=0.7)
y2 = y + bar_height
plt.barh(y2, df['col2'], height=bar_height, label='col2', align='center', alpha=0.7)
plt.yticks(y + bar_height / 2, df.index)
plt.title('col1 and col2 bar chart horizontal')
plt.legend(loc='upper right')
plt.show()

#Q3
plt.hist(MEDV, bins=20, edgecolor='black')
plt.show()

#Q4
np.random.seed(0)
data1 = np.random.rand(100)
data2 = 2 * data1 + np.random.rand(100)
plt.scatter(data1, data2, marker='o', color='blue', label='Entry 1', alpha=0.5)
plt.scatter(data1, data2, marker='o', color='red', label='Entry 2', alpha=0.5)
plt.legend()
plt.show()

#Q5
np.random.seed(1)
data1_negative = np.random.rand(100)
data2_negative = -2 * data1_negative + np.random.rand(100)
plt.scatter(data1_negative, data2_negative, marker='o', color='red', label='Entry 1', alpha=0.5)
plt.scatter(data1_negative, data2_negative, marker='o', color='purple', label='Entry 2', alpha=0.5)
plt.legend()
plt.show()
