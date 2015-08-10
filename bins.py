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
indexes = list(accumulate(indexes));
indexes = zip([0] + indexes[:-1], indexes);
bins = [[e for e in elements[s:e]] for (s, e) in indexes];
print(bins);
