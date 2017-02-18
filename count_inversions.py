def count_inversions(a, return_sorted_array=False):
    def merge_inversions(a,b):
        result = []
        i, j = 0, 0
        n = 0
        for k in range(len(a) + len(b)):
            if i == len(a):
                result.extend(b)
                break
            elif j == len(b):
                result.extend(a)
                break
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
                n += len(a) - i
        return n, result

    if len(a) <= 1:
        return 0, a

    n1, a1 = count_inversions(a[0:len(a)//2], True)
    n2, a2 = count_inversions(a[len(a)//2:], True)
    n3, a3 = merge_inversions(a1,a2)

    if return_sorted_array:
        return n1 + n2 + n3, a3
    else:
        return n1 + n2 + n3


a = [6,1,2,4,3,5]
print(count_inversions(a))