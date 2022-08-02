n = int(input())

res = 0
for _ in range(n):
    temp = input()
    num = ''

    if temp == '100':
        num = '100'
    else:
        for i in temp:
            if i == '0' or i == '6':
                num += '9'
            else:
                num += i
    res += int(num)

import math
if (res/n) - int(res/n) >= 0.5:
    print(math.ceil(res / n))
else:
    print(math.floor(res / n))





