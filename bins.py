# Initialize
elements = [0, 1, 2, 3, 4, 5, 6];
n = len(elements); # Number of elements
m = 3; # Number of bins
bins = [[] for x in range(m)];

# Precalculate this
elementsPerBinCeil = n / m;
elementsPerBinFloor = n / m - 1;
# This is the bin number above which we have to use elementsPerBinFloor
cutoffNum = n % m;
i = 0; # This is which bin to assign the element to
# Assign all elements to a bin
for element in elements:
    bins[i].append(element);
    # Move to next bin
    if (i < cutoffNum and len(bins[i]) > elementsPerBinCeil):
        i += 1;
    elif (i >= cutoffNum and len(bins[i]) > elementsPerBinFloor):
        i += 1;