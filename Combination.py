def combi(depth,start):
    if depth == r:
        print(isSelected)
        return

    for i in range(start,n):
        isSelected[depth] = number[i]
        combi(depth+1,i+1)

n = 3
r = 2
number = [1,2,3]
isSelected = [0] * r

combi(0,0)


