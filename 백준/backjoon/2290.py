s,n = input().split()
s = int(s)
row,col = s+2, (2*s) +3
def one(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0, s+1, col-1]:
            data[i].append(' ' * row)
        else:
            data[i].append(' ' * (row - 1) + '|')
    return data

def two(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0,s+1,col-1]:
            data[i].append(' '+ '-' * s + ' ')
        elif i < s+1:
            data[i].append(' ' * (row-1) + '|')
        else:
            data[i].append('|' + ' ' * (row-1))
    return data

def three(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0,s+1,col-1]:
            data[i].append(' '+ '-' * s + ' ')
        else:
            data[i].append(' ' * (row-1) + '|')
    return data

def four(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0,col-1]:
            data[i].append(' ' * row)
        elif i < s+1:
            data[i].append('|' + ' ' * (row-2) + '|')
        elif i == s+1:
            data[i].append(' '+ '-' * s + ' ')
        else:
            data[i].append(' ' * (row-1) + '|')

    return data

def five(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0,s+1,col-1]:
            data[i].append(' '+ '-' * s + ' ')
        elif i < s+1:
            data[i].append('|' + ' ' * (row-1))
        else:
            data[i].append(' ' * (row-1) + '|')
    return data

def six(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0,s+1,col-1]:
            data[i].append(' '+ '-' * s + ' ')
        elif i < s+1:
            data[i].append('|' + ' ' * (row-1))
        else:
            data[i].append('|' + ' ' * (row-2) + '|')
    return data

def seven(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i == 0 :
            data[i].append(' '+ '-' * s + ' ')
        elif i in [s+1,col-1]:
            data[i].append(' ' * row)
        else:
            data[i].append(' ' * (row-1) + '|')
    return data

def eight(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0,s+1,col-1]:
            data[i].append(' '+ '-' * s + ' ')
        else:
            data[i].append('|' + ' ' * (row-2) + '|')
    return data

def nine(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i in [0,s+1,col-1]:
            data[i].append(' '+ '-' * s + ' ')
        elif i < s+1:
            data[i].append('|' + ' ' * (row-2) + '|')
        else:
            data[i].append(' ' * (row-1) + '|')
    return data

def zero(s):
    data = [[] for _ in range(col)]
    for i in range(col):
        if i == s+1 :
            data[i].append(' ' * row)
        elif i in [0,col-1]:
            data[i].append(' '+ '-' * s + ' ')
        else:
            data[i].append('|' + ' ' * (row-2) + '|')
    return data

num = {
    '0' : zero,
    '1' : one,
    '2' : two,
    '3' : three,
    '4' : four,
    '5' : five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
}
res = [[] for _ in range(col)]
for temp in n:
    for idx,value in enumerate(num[temp](s)):
        res[idx].append(*value)
for i in res:
    print(*i)