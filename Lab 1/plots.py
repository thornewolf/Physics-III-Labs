import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

df = pd.read_excel('data.xlsx', 'Sheet1', index_col=None, na_values=['NA'])

'''print(
	df.ix[0:30, 0:2]
	)'''
print(
	df
	)

std = df.at[8,'Careful']
mean = df.at[6,'Careful']
std_range_from_mean = [mean-std,mean+std]
fraction_in_range = len([i for i in df['d (mm)'] if i<=std_range_from_mean[1] and i>=std_range_from_mean[0]])/len(df['d (mm)'])
print(
	f'Percentage of date +- 1 std: {fraction_in_range*100}%'
	)

plt.figure(0)
plt.errorbar(df['Measurment'],df['d (mm)'],yerr=df['delta d (mm)'],fmt='none',ecolor='red')
plt.scatter(df['Measurment'],df['d (mm)'],s=5)

plt.xlabel('Trial')
plt.ylabel('Measured Value (mm)')

mms = plt.axhline(y=mean+std, xmin=0, xmax=30, color='blue', ls='dashed', label="mean+-std")
mps = plt.axhline(y=mean-std, xmin=0, xmax=30, color='blue', ls='dashed')
values = df['d (mm)']
plt.yticks(np.arange(14.6, 15.6, 0.1))

plt.legend(handles=[mms])
plt.savefig('scatter.png')

plt.figure(1)
dists = [i-15.01275862 for i in df['d (mm)']]
plt.hist(dists, density=True, bins=7)
plt.xticks(np.arange(-0.4, 0.5, 0.1))
plt.savefig('histogram.png')


plt.show()



