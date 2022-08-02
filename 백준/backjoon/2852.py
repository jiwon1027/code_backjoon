n = int(input())

score = {1:0, 2:0}
temp_time = {1:0, 2:0}
answer = {1:0, 2:0}
winning_team = 0

for _ in range(n):
    team, t = input().split()
    team = int(team)
    m,s = map(int,t.split(':'))
    t = m*60 + s
    score[team] += 1

    if winning_team == 0: #처음이나 동점일 때 초기화 시키는 조건
        temp_time[team] = t
        winning_team = team
    elif winning_team != 0 and score[1] == score[2]:
        answer[winning_team] += t - temp_time[winning_team]
        winning_team = 0

if winning_team != 0: #전체시간에서
    answer[winning_team] += 60*48-temp_time[winning_team]

print('{:02d}:{:02d}'.format(answer[1]//60, answer[1]%60))
print('{:02d}:{:02d}'.format(answer[2]//60, answer[2]%60))



