from math import factorial


def fun(string, i):
    global cnt

    if i == len(data):
        cnt += 1
        if cnt == n:
            return string
    else:
        for k in data:
            if k not in string:
                res = fun(string + k, i + 1)
                if res:
                    return res
    return

while True:
    try:
        data, n = input().split()
        n = int(n)
        cnt = 0

        if factorial(len(data)) < n:
            print(data, n, '=', 'No permutation')
        else:
            print(data,n,'=',fun('',0))

    except:
        break


