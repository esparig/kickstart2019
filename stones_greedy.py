def get_energy(s, stones):
    energy = 0
    t = 0
    for e, l in stones:
        e0 = e - (t*l)
        if e0 > 0:
            energy += e0
        t += s
    return energy
# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    stones = []
    for j in range(n):
        s, e, l = [int(s) for s in input().split(" ")] # read a list of integers, 3 in this case
        stones.append((e, l))
    print("Case #{}: {}".format(i, get_energy(s, sorted( sorted(stones, key=lambda x: x[1]), key=lambda x: x[0], reverse=True))))
    # check out .format's specification for more formatting options
