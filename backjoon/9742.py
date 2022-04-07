from itertools import permutations
while True:
    try:
        data, n = input().split()
        n = int(n)
        try:
            res = ''.join(list(permutations(data))[n - 1])
            print(f'{data} {n} = {res}')

        except:
            res = 'No permutation'
            print(f'{data} {n} = {res}')
    except:
        break


