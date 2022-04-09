path = 'SSSSSSWWWNNNNNN'

distinct_path = []
length = []
start = path[0]
temp = 1

distinct_path.append(path[0])
for i in path[1:]:
    if i == start:
        temp += 1
    else:
        distinct_path.append(i)
        length.append(temp)
        start = i
        temp = 1
else:
    length.append(temp)

print(length)
print(distinct_path)

time = 0
direction = ['SE','SW','EN','ES','NW','NE','WS','WN']
vector = ['left','right','left','right','left','right','left','right']
answer = []
for i in range(len(length)-1):
    for j in range(length[i],0,-1):
        if j <= 5:
            temp_direct = distinct_path[i] + distinct_path[i + 1]
            res = 'Time ' + str(time)+ ': Go straight ' + str(j*100) + 'and turn '+ vector[direction.index(temp_direct)]
            answer.append(res)
            time += j
            break
        else:
            time += 1

print(answer)



