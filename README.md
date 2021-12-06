# Wheeler graph visualization
For EN.601.447 Computational Genomics. It has functions for creating graphs, checking whether they satisfy the Wheeler properties, and animating a visualization of the graph. It was written entirely in Python.

This README contains
1. Installation
2. Usage
    * main.py
    * benchmark.py
3. Structure


## Installation
----------------------
Use [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to install all dependencies in an environment. After cloning this repo, creating an environment, and activating the environment, run


```
conda env create --file jhu_comp_gen.yml
```

## Usage
----------------------
There are two important files:
1. [main.py](###main.py)
2. [benchmark.py](###benchmark.py)

### main.py
`main.py` runs a single simulation. It requires a `-p` input file path and `-a` approach type (`naive` or `partition`). The input file must be of our [custom file format](data/README.md). 

```
python main.py -p data/manual/wheeler.txt -a naive
```
The command above should produce this Wheeler graph

![Wheeler graph](images/wheeler-vis.png)

If the input file doesn't contain an ordering to verify or the `-no` ignore-ordering flag is used, all possible orderings are checked.
```
python main.py -p data/trie/trie.txt -a partition
```
The command above should produce this animation

![Animation](images/trie.gif)

Optional parameters include the `-no` ignore-ordering flag, `-nv` no-visualization flag, and `-l` numeric log level.

### benchmark.py
`benchmark.py` runs multiple simulations. It currently has hard-coded parameters and is used for benchmarking different approaches on different files. It saves the resulting dataframe in a csv file called `bench.csv`

## Structure
----------------------
Folder [benchmark](benchmark) contains benchmark csv files

Folder [data](data) contains all graph input files

* [manual](data/manual) contains hand-annotated graphs with orderings
* [trie](data/trie) contains tries generated with and without orderings
* [trie-input](data/trie-input) contains input files used to generate tries

Folder [images](images) contains all images used for our report.

Files [Trie](Trie.py), [trie-to-graph](trie_to_graph.py), and [generate_dna_input](generate_dna_input.py) are used to create tries

File [CreateGraph](CreateGraph.py) reads in a text file and outputs a NetworkX graph representation

File [GraphVerifier](GraphVerifier.py) takes in a NetworkX graph with a given ordering and verifies if it is Wheeler, using either the naive or partition approach.

File [visualize](visualize.py) contains all the drawing-related functions

File [main](main.py) and [benchmark](benchmark.py) house the main driver code and the benchmarking suite.
