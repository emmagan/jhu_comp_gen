import sys
import random

num_lines = int(sys.argv[1])
char_per_line = int(sys.argv[2])
file = open(sys.argv[3], "w")

dna = "ACGT"

for i in range(num_lines):
    for j in range(char_per_line):
        index = random.randint(0, 3)
        file.write(dna[index])
    file.write("\n")

file.close()

