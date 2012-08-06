import itertools

perm = list(itertools.permutations(range(10), 10))
print perm[1000000-1]
