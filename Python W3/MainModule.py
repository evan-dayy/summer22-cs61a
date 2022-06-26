import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

arr2 = np.array([[1,2,3,4],
                 [1,2,3,5]])
arr2_view = arr2.view()
arr2_copy = arr2.copy()
print(arr2_copy.base)
print(arr2_view.base)

print(arr2.dtype)
print(arr2.astype('S'))

print(arr2.reshape(-1))
print(arr2)

nditerator = np.nditer(arr2)
for i in nditerator:
    print(i)


nditerator_ex = np.nditer(arr2, flags = ['buffered'], op_dtypes = ['S'])
for i in nditerator_ex:
    print(i)

for x in np.nditer(arr2[:, ::2]):
  print(x)

for ind, i in np.ndenumerate(arr2):
    print(ind, i)

# ---

arr1 = np.array([1, 2])
arr2 = np.array([5, 6])
print("--------------------------------")
arr = np.concatenate((arr1, arr2), axis=0) # for 1-D, it cannot be axis = 1
print(arr)
print("--------------------------------")
arr = np.stack((arr1, arr2), axis=1) # for 1-D, it can use stack
print(arr)
print("--------------------------------")
arr = np.hstack((arr1, arr2)) # row-along stack
print(arr)
print("--------------------------------")
arr = np.vstack((arr1, arr2)) # column-along stack
print(arr)
print("--------------------------------")
arr = np.dstack((arr1, arr2)) # deepth-along stack
print(arr)

# ----
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5], hist = False)
plt.show()

from numpy import random
x = random.choice([1,2,3,4,5,-1,-3], p = [0.1,0.2,0.3,0.1,0.1,0.1,0.1],
                  size = (100))
print(x)
#sns.displot(x, hist = False)
#plt.show()

# -----
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc = 1, scale = 10, size=1000), hist=False)

plt.show()

# -----
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.9, size=1000), hist=True, kde=False)

plt.show()

# ------ ufunc
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)
