import collections

def can_form_palindrome(str):
    counts = collections.Counter(str)
    vals = counts.values()
    parity = collections.Counter([n%2 for n in vals])
    odds = parity[1]
    if  odds == 0:
        return 1
    elif odds == 1 and len(str)%2 == 1:
        return 1
    else:
        return 0

    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n, q = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
  blocks = input()
  #print(n,q,blocks)
  counter = 0
  for j in range(q):
      f, t = [int(s) for s in input().split(" ")]
      counter += can_form_palindrome(blocks[f-1:t])
  print("Case #{}: {}".format(i, counter))
  # check out .format's specification for more formatting options
