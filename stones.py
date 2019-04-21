import queue as Q

class Stone:
    def __init__(self, s, e, l):
        self.s = s
        self.e = e
        self.l = l

class Node:
    def __init__(self, stones, energy):
        self.stones = stones
        self.energy = energy

def decay(stones, selected):
    new_stones = []
    for i in range(len(stones)):
        if i != selected:
            cur_energy = stones[i].e-(stones[selected].s*stones[i].l)
            if cur_energy > 0:
                new_stones.append(Stone(stones[i].s, cur_energy, stones[i].l))
    return new_stones

def max_energy(stones):
    return sum([s.e for s in stones])

def get_energy(stones):
    my_q = Q.PriorityQueue()
    my_q.put((-max_energy(stones), Node(stones, 0) ))
    max_e = 0
    count = 0
    while not my_q.empty():
        count += 1
        #print("iter:", count)
        cur = my_q.get_nowait()
        #print(cur)
        #print("is", -cur[0],"greater than", max_e)
        if -cur[0] > max_e:
            for i in range(len(cur[1].stones)):
                new_stones = decay(cur[1].stones, i)
                #print("new size stones", len(new_stones))
                consumed_energy = cur[1].energy + cur[1].stones[i].e
                #print("consumed", consumed_energy)
                if max_e < consumed_energy:
                    max_e = consumed_energy
                if len(new_stones) > 0:
                    #print("entra")
                    my_q.put((-(max_energy(new_stones)+consumed_energy), Node(new_stones, consumed_energy) ))
        else:
            pass
    return max_e

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    stones = []
    for j in range(n):
        s, e, l = [int(s) for s in input().split(" ")] # read a list of integers, 3 in this case
        stones.append(Stone(s, e, l))
    print("Case #{}: {}".format(i, get_energy(stones)))
# check out .format's specification for more formatting options
