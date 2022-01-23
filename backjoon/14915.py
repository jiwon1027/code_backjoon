m,n = map(int,input().split())

def solution(n, q):
    rev_base = ''
    if n == 0:
        return 0
    while n > 0:
        n, mod = divmod(n, q)
        data = [10,11,12,13,14,15]
        alphabet = ['A','B','C','D','E','F']

        if mod in data:
            mod = alphabet[data.index(mod)]

        rev_base += str(mod)

    return rev_base[::-1]

print(solution(m, n))