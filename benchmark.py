from timeit import timeit
import os
import pandas as pd
from functools import partial
from main import ordering, no_ordering

data = {}
path = 'data/manual'
dirs = os.listdir( path )
for fname in dirs:
    file = os.path.join(path, fname)
    ntime = timeit(partial(ordering, file, False, 'naive'), number=10) # args are path, vis, approach
    ptime = timeit(partial(ordering, file, False, 'partition'), number=10) # args are path, vis, approach
    data[fname] = [ntime, ptime]
df = pd.DataFrame.from_dict(data, orient='index', columns=['naive', 'partition'])
print(df)
