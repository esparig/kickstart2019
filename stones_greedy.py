# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    stones = []
    for j in range(n):
        s, e, l = [int(s) for s in input().split(" ")] # read a list of integers, 3 in this case
        stones.append((e, l))
    st = sorted(stones, key=lambda x: x[1])
    print(st)
    print(stones)
    print(sorted( st, reverse=True))
    print("Case #{}: {}".format(i, 0))
# check out .format's specification for more formatting options
