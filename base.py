from collections import defaultdict as ddic, deque
from itertools import combinations, permutations, product
import sys
sys.setrecursionlimit(10**6) #or 10**7
stdout = sys.stdout
rs = lambda: input().strip() # read string
ri = lambda: int(input()) # read integer
rli= lambda: [int(s) for s in input().strip().split(" ")] # read list of integers

def IsApproximatelyEqual(x, y, epsilon):
          """Returns True if y is within relative or absolute 'epsilon' of x.

          By default, 'epsilon' is 1e-6.
          """
          # Check absolute precision.
          if -epsilon <= x - y <= epsilon:
          return True

          # Is x or y too close to zero?
          if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
          return False

          # Check relative precision.
          return (-epsilon <= (x - y) / x <= epsilon
          or -epsilon <= (x - y) / y <= epsilon)

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = ri() # read a line with a single integer
for i in range(1, t + 1):
  n, m = rli() # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
