n,m = map(int,input().split(':'))

import math
gcd = math.gcd(n,m)

s = f'{int(n/gcd)}:{int(m/gcd)}'
print(s)