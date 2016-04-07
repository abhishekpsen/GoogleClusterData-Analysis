__author__ = 'Shruthi Hiremath'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:\AIC\Project\googleclusterdata.csv')

x=  df[['Time','JobType']]
x_time = x['Time']
#print x_time

y=df[['NrmlTaskMem','JobType']]
y_0 = y.where(y['JobType'] ==0)
y_Job0 = y_0['NrmlTaskMem']

y_1 = y.where(y['JobType'] ==1)
y_Job1 = y_1['NrmlTaskMem']

y_2 = y.where(y['JobType'] ==2)
y_Job2 = y_2['NrmlTaskMem']

y_3 = y.where(y['JobType'] ==3)
y_Job3 = y_3['NrmlTaskMem']


J0= plt.scatter(x_time,y_Job0,  c='b',marker='o',  label='Job 0')
J1= plt.scatter(x_time,y_Job1,  c='g',marker='+',   label='Job 1')
J2 =plt.scatter(x_time,y_Job2,  c='r',marker='*',  label='Job 3')
J3 =plt.scatter(x_time,y_Job3,  c='m',marker='^',   label='Job 4')

#plt.savefig('NrmlTaskMem.png')


plt.legend((J0,J1,J2,J3),('Job0', 'Job1', 'Job2', 'Job3'), fontsize=8)


plt.show()