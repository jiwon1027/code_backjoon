
# target = [2,2,2,2,2]
target = [2 ,3 ,4 ,3 ,2]
positions = [[0 ,0] ,[0 ,1] ,[1 ,1] ,[-3 ,5] ,[7 ,5] ,[10 ,0] ,[-15 ,22] ,[-6 ,-5] ,[3 ,3] ,[5 ,-5]]



def solution(target, positions):
    std = [0, 0]
    data = []
    temp = 0
    score = [10, 8, 6, 4, 2, 0]
    for i in range(len(target)):
        temp += target[i]
        data.append(temp)
    res = 0
    import math
    from bisect import bisect_left
    for x, y in positions:
        temp = math.sqrt((std[0] - x) ** 2 + (std[1] - y) ** 2)
        res += score[bisect_left(data, temp)]

    return res







