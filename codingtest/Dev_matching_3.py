def solution(k):
    global res

    data = [6,2,5,5,4,5,6,3,7,6]
    res = 0

    def dfs(depth,k,data):
        global res

        if depth > 25:
            return

        if k <= 0:
            if k == 0:
                res+=1
            return

        if depth == 0:
            if k == 6:
                res += 1
            for i in range(1,10):
                dfs(depth+1,k-data[i],data)
        else:
            for i in range(10):
                dfs(depth+1,k-data[i],data)

    dfs(0,k,data)

    return res



print(solution(6))