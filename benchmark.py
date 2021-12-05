from timeit import timeit
import os
import pandas as pd
from functools import partial
from main import ordering, no_ordering
from CreateGraph import parse_file

data = {}
path = 'data/manual'
dirs = os.listdir( path )
for fname in dirs:
    file = os.path.join(path, fname)
    input = parse_file(file)

    notime = timeit(partial(ordering, input, False, 'naive'), number=10) # args are path, vis, approach
    potime = timeit(partial(ordering, input, False, 'partition'), number=10)
    #ntime = timeit(partial(no_ordering, input, False, 'naive'), number=1) # args are path, vis, approach
    #ptime = timeit(partial(no_ordering, input, False, 'partition'), number=1)

    data[fname] = [notime, potime]#, ntime, ptime]
df = pd.DataFrame.from_dict(data, orient='index', columns=['naive-order', 'partition-order'])#, 'naive', 'partition'])
print(df)
