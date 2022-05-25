n = int(input())
c = []
for _ in range(n):
    c.append(input())
n = int(input())
x = []
for _ in range(n):
    x.append(int(input()))
n = int(input())
y = []
for _ in range(n):
    y.append(int(input()))
m = int(input())
q = []
for _ in range(n):
    q.append(input())
print(c)
print(x)
print(y)
print(q)
'''
#브루트포스
res = []
for name in q:
    idx = c.index(name) #기준
    index, temp = idx, 10 ** 9
    for i in range(n):
        if idx != i:
            if x[i] == x[idx]:
                if temp > abs(y[i]-y[idx]):
                    index = i
                    temp = abs(y[i]-y[idx])

                elif temp == abs(y[i] - y[idx]):
                    if c[index] > c[i]:
                        index = i

            if y[i] == y[idx]:
                if temp > abs(x[i]-x[idx]):
                    index = i
                    temp = abs(x[i]-x[idx])

                elif temp == abs(x[i] - x[idx]):
                    if c[index] > c[i]:
                        index = i
    if index == idx:
        print('NONE')
    else:
        print(c[index])
'''


# 시뮬레이션(queue, dict 이용)
'''
data = dict()
for i in range(len(c)):
    data[c[i]] = x[i],y[i]
print(data)

from collections import deque

res = []
for idx, city in enumerate(q):
    queue = deque()
    std_x, std_y = data[city][0], data[city][1]
    for key,value in data.items():
        if key != city and (std_x == value[0] or std_y == value[1]):
            queue.append((key, value[0], value[1]))
    if len(queue) > 0: #여기 이분탐색으로 고쳐보자
        min_dict = dict()
        while queue:
            temp_city, temp_x, temp_y = queue.popleft()
            min_dict[temp_city] = abs(std_x - temp_x) + abs(std_y - temp_y)

        res.append(sorted(min_dict.items(),key = lambda x : x[1])[0][0])
    else:
        res.append('NONE')
print(res)
'''

# 이분탐색 해보려다가 최소값만 찾는거니까 똑같은 시간복잡도인 heapq 사용해봄
'''
data = dict()
for i in range(len(c)):
    data[c[i]] = x[i],y[i]
print(data)

import heapq
res = []

for idx, city in enumerate(q):
    heapq_list = []
    std_x, std_y = data[city][0], data[city][1]
    for key,value in data.items():#여기 이분탐색으로 고쳐보자
        if key != city and (std_x == value[0] or std_y == value[1]):
            heapq.heappush(heapq_list, (abs(std_x - value[0]) + abs(std_y - value[1]), key))

    if len(heapq_list) > 0:
        temp_value, ans = heapq.heappop(heapq_list)

        while heapq_list:
            temp, temp_city = heapq.heappop(heapq_list)
            if temp == temp_value:
                ans = min(ans, temp_city)
            else:
                break
        res.append(ans)

    else:
        res.append('NONE')
print(res)
'''
data_x = dict()
for i in range(len(c)):
    data_x[(x[i], y[i])] = c[i]

data_y = dict()
for i in range(len(c)):
    data_y[(y[i], x[i])] = c[i]

name = dict()
for i in range(len(c)):
    name[c[i]] = (x[i], y[i])


from bisect import bisect_left, bisect_right
x_sort_data = sorted(list(data_x.keys()), key=lambda x : x[0])
y_sort_data = sorted(list(data_y.keys()), key=lambda x : x[1])


for city in q:
    temp = 0
    temp_city = ''
    temp_x, temp_y = name[city]

    x_left = bisect_left(x_sort_data, (temp_x,temp_y))
    x_right = bisect_right(x_sort_data, (temp_x,temp_y))

    y_left = bisect_left(y_sort_data,(temp_y,temp_x))
    y_right = bisect_right(y_sort_data,(temp_y,temp_x))


    fun_a = x_sort_data[x_left-1]
    if temp_x == fun_a[0]:
        if temp > abs(fun_a[1] - temp_y):
            temp_city = data_x[fun_a]
            temp = abs(fun_a[1] - temp_y)

    if x_right < len(x_sort_data):
        fun_b = x_sort_data[x_right]
        if temp_x == fun_b[0]:
            if temp > abs(fun_b[1] - temp_y):
                temp_city = data_x[fun_b]
                temp = abs(fun_b[1] - temp_y)


    fun_c = y_sort_data[x_left-1]
    if temp_y == c[0]:
        if temp > abs(fun_c[1] - temp_x):
            temp_city = data_x[fun_c]
            temp = abs(fun_c[1] - temp_x)

    if y_right < len(y_sort_data):
        fun_d = y_sort_data[x_right]
        if temp_y == fun_d[0]:
            if temp > abs(fun_d[1] - temp_x):
                temp_city = data_x[fun_d]
                temp = abs(fun_d[1] - temp_x)

    print(temp_city)


