def ispalindrome(data):
    data_reverse = data[::-1]
    if data == data_reverse:
        return 1
    else:
        return 0

data = input()
res = []
from itertools import permutations
for i in permutations(data,int(len(data))):
    temp = ''
    if ispalindrome(i):
        for j in range(int(len(data))):
            temp += i[j]
        res.append(temp)
if len(res) == 0:
    print("I'm Sorry Hansoo")
else:
    print(min(res))