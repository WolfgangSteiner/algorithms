from quick_sort import *

def read_input(fn): return [int(l) for l in open(fn).readlines()]

results = {10:(25,29,21), 100:(615,587,518), 1000:(10297,10184,8921)}
pivot_funcs = (first_pivot, last_pivot, median_of_three_pivot)


for n in 10,100,1000:
    data = read_input(str(n) + ".txt")
    for idx, pivot_func in enumerate(pivot_funcs):
        assert quick_sort(list(data), pivot_func) == results[n][idx]


data = read_input("assignment_1_3_input.txt")
print([quick_sort(list(data), pf) for pf in pivot_funcs])
