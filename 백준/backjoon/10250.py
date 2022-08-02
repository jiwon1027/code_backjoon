t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split())

    room = n//h
    floor = n%h
    if floor == 0:
        floor = h
        print(floor,end='')
        print('{0:02d}'.format(room))
    else:
        print(floor,end='')
        print('{0:02d}'.format(room+1))
