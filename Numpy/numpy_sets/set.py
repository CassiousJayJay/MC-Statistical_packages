import numpy as np

set1 = np.array([1, 2, 4, 3, 5, 7])
set2 = np.array([0, 3, 4, 8, 9, 10])
# find the union of set
union_set = np.union1d(set1, set2)
# fnding the intersection of a set
intersection = np.intersect1d(set1, set2)
# set difference
set_differnce = np.setdiff1d(set1, set2)
# symmetric difference of two arrays
diff = np.setxor1d(set1, set2)

print("Union of a set: \n", union_set)
print("Intersection: \n", intersection)
print("Set difference: \n", set_differnce)
print("Symetric of a set: \n", diff)
