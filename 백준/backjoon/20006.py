p,m = list(map(int,input().split()))
player = []
for _ in range(p):
    level, id = input().split()
    player.append([int(level), id])
rooms = []
#시간순으로 room을 출력해야하니까 room자체를 스택으로 할 필요가 있었음
#dp로 그냥 하려고 했는데 방 만든 순서로 하려니까 구현이 힘들었음

for lv, id in player:
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m:
            continue
        if rooms[i][0]-10 <= lv <= rooms[i][0]+10:
            rooms[i][1].append((lv,id))
            break
    else:
        rooms.append([lv,[(lv,id)]])

for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
        res = sorted(rooms[i][1],key=lambda x:x[1])
        for j in range(m):
            print(*res[j])
    else:
        print('Waiting!')
        res = sorted(rooms[i][1],key=lambda x:x[1])
        for j in range(len(res)):
            print(*res[j])