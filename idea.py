l1 = [1,2,3,4,5]

from functools import reduce

k = reduce(lambda x, y: x*y, l1)
print(k)
k=1
for i in l1:
    k*=i
print(k)