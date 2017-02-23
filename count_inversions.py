def count_inversions(a, return_sorted_array=False):
    def merge_inversions(a,b):
        result = []
        i, j = 0, 0
        n = 0
        for k in range(len(a) + len(b)):
            if i == len(a):
                result.extend(b[j:])
                break
            elif j == len(b):
                result.extend(a[i:])
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
        if return_sorted_array:
            return 0, a
        else:
            return 0

    n1, a1 = count_inversions(a[0:len(a)//2], True)
    n2, a2 = count_inversions(a[len(a)//2:], True)
    n3, a3 = merge_inversions(a1,a2)

    if return_sorted_array:
        return n1 + n2 + n3, a3
    else:
        return n1 + n2 + n3


if __name__ == "__main__":

    assert count_inversions([1]) == 0
    assert count_inversions([2,1]) == 1
    assert count_inversions([1,2]) == 0
    assert count_inversions([3,1,2]) == 2
    assert count_inversions([3,2,1]) == 3
    assert count_inversions([1,2,4,3]) == 1
    assert count_inversions([3,1,2,4]) == 2
    assert count_inversions([3,1,4,2]) == 3
    assert count_inversions([1,2,4,3,5]) == 1
    assert count_inversions([6,1,2,4,3,5]) == 6

    a2 = [ 9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0 ]
    assert count_inversions(a2) == 56

    a3 = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39,
         51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15,
         92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71,
         47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30,
         22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54]
    assert count_inversions(a3) == 2372
