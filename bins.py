# Python 3.4.3
from itertools import *;

# Initialize
elements = [0, 1, 2, 3, 4, 5, 6];
n = len(elements); # Number of elements
m = 3; # Number of bins

# Precalculate this
cutoffNum = n % m;
# Assign all elements to a bin
indexes = [n // m + 1] * cutoffNum + [n // m] * (m - cutoffNum);
binNums = chain.from_iterable([[i] * indexes[i] for i in range(0, m)]);
labeledElements = zip(binNums, elements);
bins = [list(list(zip(*v))[1]) for k, v in groupby(labeledElements, lambda x: x[0])]
print(bins);
