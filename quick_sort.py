import numpy as np
import random
import time

def first_pivot(a):
    return 0


def last_pivot(a):
    return len(a) - 1


def random_pivot(a):
    return random.randint(0,len(a)-1)


def median_of_three_pivot(a):
    i1, i2, i3 = 0, (len(a) - 1)//2, -1
    p = ((a[i1],i1), (a[i2],i2), (a[i3],i3))
    return sorted(p, key=lambda x: x[0])[1][1]


def quick_sort(a, pivot_func=random_pivot):
    def partition(a, pivot_func):
        pivot_idx = pivot_func(a)
        a[0],a[pivot_idx] = a[pivot_idx],a[0]
        i = j = 1
        while j < len(a):
            if a[j] > a[0]:
                pass
            else:
                a[i],a[j] = a[j],a[i]
                i+=1
            assert a[i-1] <= a[0]
            j+=1
        a[0],a[i-1] = a[i-1],a[0]
        return i-1

    if len(a) <= 1:
        return 0

    n0 = len(a) - 1
    idx = partition(a, pivot_func)
    n1 = quick_sort(a[0:idx], pivot_func)
    n2 = quick_sort(a[idx+1:], pivot_func)
    return n0 + n1 + n2


if __name__ == "__main__":
    def time_quick_sort(a,pivot_func):
        start_time = time.time()
        print(pivot_func.__name__)
        quick_sort(a, pivot_func)
        print("Time: %.2f" % (time.time() - start_time))

    a1 = np.sort(np.random.random(random.randint(0, 10000)))
    a2 = np.copy(a1)
    time_quick_sort(a1,choose_first)
    time_quick_sort(a2,choose_random_pivot)




