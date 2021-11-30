from timeit import timeit
import os
from functools import partial
from main import ordering, no_ordering

path = 'data/manual'
dirs = os.listdir( path )
for fname in dirs:
    file = os.path.join(path, fname)

print(timeit(partial(ordering, file, False, 'naive'), number=5)) # args are path, vis, approach
print(timeit(partial(ordering, file, False, 'partition'), number=5)) # args are path, vis, approach