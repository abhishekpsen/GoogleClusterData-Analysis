import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../googleclusterdata.csv')

byparentid = df.groupby('ParentID')

maxtimestamps = byparentid.agg({'Time':np.max})
mintimestamps = byparentid.agg({'Time':np.min})

jobtimes = maxtimestamps - mintimestamps
jobtimes.hist()
plt.savefig('JobTimes.png')

jobtaskcounts = byparentid.agg({'TaskID':'count'})

jobtaskcounts = jobtaskcounts.rename(columns = {'TaskID': 'TaskCount'})

jobtaskcountslt1000 = jobtaskcounts[jobtaskcounts.TaskCount < 1000]

print len(jobtaskcountslt1000)

jobtaskcountslt1000.hist(bins=20)
plt.savefig('JobTaskslt1000.png')

plt.show()