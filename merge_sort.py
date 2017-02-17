import numpy as np

def merge_sort(a):
    def merge(a, b):
        result = []
        i, j = 0, 0
        while True:
            if i == len(a):
                result.extend(b[j:])
                break
            elif j == len(b):
                result.extend(a[i:])
                break
            elif a[i] <= b[j]:
                result.append(a[i])
                i+=1
            else:
                result.append(b[j])
                j+=1

        return result

    if len(a) == 1:
        return a

    p1 = 0
    q1 = len(a) // 2
    p2 = q1
    q2 = len(a)

    return merge(merge_sort(a[p1:q1]), merge_sort(a[p2:q2]))



a = np.random.random(10000)
result = merge_sort(a)
assert np.all(result == np.sort(a))
