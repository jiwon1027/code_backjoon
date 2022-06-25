for _ in range(int(input())):
    #팀 개수, 문제 개수, 팀id, 로그 엔트리 개수
    n,k,id_t,m = list(map(int,input().split()))
    score = [[0 for i in range(k)] for j in range(n)]
    count = [0]*n
    time = [0]*n
    for question in range(1,m+1):
        #팀 id, 문제 번호, 획득한 점수
        i,j,s = list(map(int,input().split()))
        if score[i-1][j-1] < s:
            score[i-1][j-1] = s
        count[i-1] += 1
        time[i-1] = question

    final = [[sum(score[i]), count[i], time[i]] for i in range(n)]
    ans = final[id_t-1]

    final.sort(key = lambda x : (x[0],-x[1],-x[2]),reverse=True)
    #print(final)

    for i in range(n):
        if(ans == final[i]):
            print(i+1)
            break
