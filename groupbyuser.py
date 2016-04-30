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


print sorted(listdir('task_events'))[-1]

task_events_csv_colnames = ['time', 'missing', 'job_id', 'task_idx', 'machine_id', 'event_type', 'user', 'sched_cls',
                            'priority', 'cpu_requested', 'mem_requested', 'disk', 'restriction']
task_event_df = read_csv(path.join('task_events', 'part-00499-of-00500.csv.gz'), header=None, index_col=False,
                         compression='gzip', names=task_events_csv_colnames)
seed(83)

temp_df = task_event_df
num = 1
# Not the most elegant code I've ever written...

for fn in sorted(listdir('task_events')):

    fp = path.join('task_events', fn)
    task_events_df = read_csv(fp, header=None, index_col=False, compression='gzip',
                              names=task_events_csv_colnames)

    temp_df.append(task_event_df)


print "LOOP OVER \n"
temp_df_group = temp_df.groupby('user')['index'].count()
temp_df_group.to_csv("file1.csv", sep=',', encoding='utf-8')

temp_df.plot(kind='bar')
plt.show()
plt.savefig("usage 0-50.png")

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