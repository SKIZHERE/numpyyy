import sys
import time
import numpy as np

# a=np.array([1,3,6])
# print(a[0])

"""
l = range(100)
print(sys.getsizeof(5)*len(l))

arr = np.arange(100)
print(arr.size*arr.itemsize)
"""

num = 100000000
l1 = range(num)
l2 = range(num)

a1 = np.arange(num)
a2 = np.arange(num)

start1 = time.time()
result1 = [x+y for x, y in zip(l1, a1)]
print(time.time()-start1)

start2 = time.time()
result2 = a1+a2
print(time.time()-start2)