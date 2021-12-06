from timeit import timeit
import os
import argparse
import pandas as pd
from functools import partial
from main import ordering, no_ordering
from CreateGraph import parse_file

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', dest='path', help='Output file path name', default='benchmark/bench.csv')
parser.add_argument('-r', '--repetitions', dest='repetitions', help='Number of repetitions to run each function for', default=10, type=int)
parser.add_argument('-m', '--max_nodes_manual', dest='mnodes', help='Maximum number of nodes in the hand-annotated graphs for running the benchmarking', default=11, type=int)
parser.add_argument('-t', '--max_nodes_trie', dest='tnodes', help='Maximum number of nodes in the tries for running the benchmarking', default=390, type=int)
args = parser.parse_args()

data = {}

# All data in manual folder has an ordering already.
path = 'data/manual'
dirs = os.listdir( path )
for fname in dirs:
    file = os.path.join(path, fname)
    input = parse_file(file)

    notime = timeit(partial(ordering, input, False, 'naive'), number=args.repetitions) # args are path, vis, approach
    potime = timeit(partial(ordering, input, False, 'partition'), number=args.repetitions)
    if len(input[0]) < args.mnodes:
        ntime = timeit(partial(no_ordering, input, False, 'naive'), number=args.repetitions) # args are path, vis, approach
        ptime = timeit(partial(no_ordering, input, False, 'partition'), number=args.repetitions)
    else:
        ntime = ptime = None

    data[fname] = [notime, potime, ntime, ptime]

path = 'data/trie'
dirs = os.listdir( path )
for fname in dirs:
    file = os.path.join(path, fname)
    input = parse_file(file)

    # if the file already has an ordering, we can verify the ordering
    if len(input[2]) == 0:
        notime = potime = None
    else:
        notime = timeit(partial(ordering, input, False, 'naive'), number=args.repetitions) # args are path, vis, approach
        potime = timeit(partial(ordering, input, False, 'partition'), number=args.repetitions)

    # compute the ordering ourselves
    if len(input[0]) < args.tnodes:
        ntime = timeit(partial(no_ordering, input, False, 'naive'), number=args.repetitions) # args are path, vis, approach
        ptime = timeit(partial(no_ordering, input, False, 'partition'), number=args.repetitions)
    else:
        ntime = ptime = None

    data[fname] = [notime, potime, ntime, ptime]

df = pd.DataFrame.from_dict(data, orient='index', columns=['naive-order', 'partition-order', 'naive', 'partition'])
#print(df)
df.to_csv(args.path)  
