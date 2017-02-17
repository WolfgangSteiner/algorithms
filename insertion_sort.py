import numpy as np

def insertion_sort(a):
    if len(a) == 1:
        return a

    result = np.copy(a)
    for i in range(1,len(a)):
        x = result[i]
        j = i - 1
        while j >= 0 and result[j] > x:
            result[j+1] = result[j]
            j-=1

        result[j+1] = x

    return result


a = np.random.random(10000)
assert np.all(insertion_sort(a) == np.sort(a))