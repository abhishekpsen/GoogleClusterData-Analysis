from __future__ import division
from os import listdir, chdir, path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from random import randint, sample, seed
from collections import OrderedDict
from pandas import DataFrame
import operator


from random import random
from math import ceil as _ceil, log as _log
'''
def xsample(population, k):
    """A generator version of random.sample"""
    print "population:"
    print population
    n = len(population)
    if not 0 <= k <= n:
        raise ValueError, "sample larger than population"
    _int = int
    setsize = 21        # size of a small set minus size of an empty list
    if k > 5:
        setsize += 4 ** _ceil(_log(k * 3, 4)) # table size for big sets
    if n <= setsize or hasattr(population, "keys"):
        # An n-length list is smaller than a k-length set, or this is a
        # mapping type so the other algorithm wouldn't work.
        pool = list(population)
        for i in xrange(k):         # invariant:  non-selected at [0,n-i)
            j = _int(random() * (n-i))
            yield pool[j]
            pool[j] = pool[n-i-1]   # move non-selected item into vacancy
    else:
        try:
            selected = set()
            selected_add = selected.add
            for i in xrange(k):
                j = _int(random() * n)
                while j in selected:
                    j = _int(random() * n)
                selected_add(j)
                yield population[j]
        except (TypeError, KeyError):   # handle (at least) sets
            if isinstance(population, list):
                raise
            for x in sample(tuple(population), k):
                yield x


'''
def lrange(num1, num2 = None, step = 1):
    op = operator.__lt__

    if num2 is None:
        num1, num2 = 0, num1
    if num2 < num1:
        if step > 0:
            num1 = num2
        op = operator.__gt__
    elif step < 0:
        num1 = num2

    while op(num1, num2):
        yield num1
        num1 += step
#df = pd.read_csv('../googleclusterdata.csv')


files = sorted(listdir('task_events'))
filelist = files[0:51]
task_events_csv_colnames = ['user','count']
file_csv_colnames = ['time', 'missing', 'job_id', 'task_idx', 'machine_id', 'event_type', 'user', 'sched_cls',
                            'priority', 'cpu_requested', 'mem_requested', 'disk', 'restriction']
#task_event_df = read_csv(path.join('task_events', 'part-00499-of-00500.csv.gz'), header=None, index_col=False,
#                         compression='gzip', names=task_events_csv_colnames)
seed(83)


num = 1
# Not the most elegant code I've ever written...


task_events_df = read_csv("file1.csv", header=None, index_col=False,
                              names=task_events_csv_colnames)



print task_events_df
count=0
temp_dict = {}
'''
for row in task_events_df.iterrows():
        index,data = row
        user = data['user']
        '''
user = "fJYeclskJqPWsAT6TX/r9X5OiIZpSEb2PBGliYAOMxM="
print "user : %s" %user
new_df_columns = ['event_type']
new_df_index = np.arange(2) # array of numbers for the number of samples
new_df = pd.DataFrame(columns=new_df_columns)
event0=0
event1=0
event2=0
event3=0
event4=0
event5=0
event6=0
event7=0
event8=0
for fn in filelist:

    fp = path.join('task_events', fn)
    file_df = read_csv(fp, header=None, index_col=False, compression='gzip',
                      names=file_csv_colnames)
    print fn
    print
    for row1 in file_df.iterrows():
        index1,data1 = row1
        #print "user1 : %s" %data1['user']
        if data1['user'] == user:
            #print "in if"

            event_no = int(data1['event_type'])
            if event_no == 0:
                event0+=1
            elif event_no == 1:
                event1+=1
            elif event_no == 2:
                event2+=1
            elif event_no == 3:
                event3+=1
            elif event_no == 4:
                event4+=1
            elif event_no == 5:
                event5+=1
            elif event_no == 6:
                event6+=1
            elif event_no == 7:
                event7+=1
            elif event_no == 8:
                event8+=1
            count = count + 1
            #print event_no
            #print


temp_dict[user] = {'SUBMIT' : event0,
                   'SCHEDULE' : event1,
                   'EVICT' : event2,
                   'FAIL' : event3,
                   'FINISH' : event4,
                   'KILL' : event5,
                   'LOST' : event6,
                   'UPDATE_PENDING' : event7,
                   'UPDATE_RUNNING' : event8}
temp_df = pd.DataFrame(temp_dict.values())
#new_df.append(temp_df,ignore_index=True)
temp_df.to_csv("0-50.csv", sep=',', encoding='utf-8')
print temp_df
temp_df.plot(kind='bar')
plt.show()
plt.savefig("userevents.png")

#task_events_df.hist('user',weights=task_events_df['count'] )

print "LOOP OVER \n"
#temp_df_group = temp_df.groupby('user')['time'].count()
#temp_df_group.to_csv("file1.csv", sep=',', encoding='utf-8')

'''

#%%time
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(samples_df['time'], samples_df['cpu_requested'], label='cpu requested')
ax.plot(samples_df['time'], samples_df['mem_requested'], label='mem requested')
plt.xlim(min(samples_df['time']), max(samples_df['time']))
plt.legend()
plt.show()
'''