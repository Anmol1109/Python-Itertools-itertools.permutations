# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
a, b = input().split()
for i in permutations(sorted(a),int(b)):
    print("".join(i))
