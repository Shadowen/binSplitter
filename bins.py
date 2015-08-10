# Initialize
elements = [0, 1, 2, 3, 4, 5, 6];
n = len(elements); # Number of elements
m = 3; # Number of bins
bins = [[] for x in range(m)];

# Precalculate this
cutoffNum = n % m;
# Assign all elements to a bin
indexes = [n / m + 1] * cutoffNum + [n / m] * (m - cutoffNum);
def accumulate(i, acc=[0]):
    acc[0] += i;
    return acc[0];
indexes = map(accumulate, indexes);
indexes = zip([0] + indexes[:-1], indexes)
bins = [[e for e in elements[s:e]] for (s, e) in indexes];
print(bins)
