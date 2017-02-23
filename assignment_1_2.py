from count_inversions import count_inversions

with open("input.txt") as f:
    a = [int(l) for l in f.readlines()]

print(count_inversions(a))