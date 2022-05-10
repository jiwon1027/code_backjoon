atoms = [[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]

def solution(atoms):
    res = 0
    flag = 0
    for i,j in atoms:
        #print(i,j,flag)
        if i >= 81 or j >= 36:
            if flag:
                flag = 0
            else:
                res += 1
                flag = 1

        elif i >= 151 and j >= 76:
            res += 1
            flag = 0
        else:
            flag = 0
        #print(res)
    return res

print(solution(atoms))
