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
    if len(input[0]) < 11:
        ntime = timeit(partial(no_ordering, input, False, 'naive'), number=10) # args are path, vis, approach
        ptime = timeit(partial(no_ordering, input, False, 'partition'), number=10)
    else:
        ntime = ptime = None

    data[fname] = [notime, potime, ntime, ptime]

path = 'data/trie'
dirs = os.listdir( path )
for fname in dirs:
    file = os.path.join(path, fname)
    input = parse_file(file)

    if len(input[2]) == 0:
        notime = potime = None
    else:
        ntime = timeit(partial(no_ordering, input, False, 'naive'), number=10) # args are path, vis, approach
        ptime = timeit(partial(no_ordering, input, False, 'partition'), number=10)

    if len(input[0]) < 390:
        ntime = timeit(partial(no_ordering, input, False, 'naive'), number=10) # args are path, vis, approach
        ptime = timeit(partial(no_ordering, input, False, 'partition'), number=10)
    else:
        ntime = ptime = None

    data[fname] = [notime, potime, ntime, ptime]

df = pd.DataFrame.from_dict(data, orient='index', columns=['naive-order', 'partition-order', 'naive', 'partition'])
print(df)
df.to_csv('benchmark/bench.csv')  
