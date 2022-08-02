from itertools import permutations
from math import factorial


while True:
    try:
        s, loc = input().split()
        loc = int(loc)

        if loc > factorial(len(s)):
            r = 'No permutation'
        else:
            p = permutations(s)
            for _ in range(loc - 1):
                next(p)

            r = ''.join(next(p))

        result = f'{s} {loc} = {r}'

        print(result)
    except:
        break