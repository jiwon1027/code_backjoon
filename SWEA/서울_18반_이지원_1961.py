'''
python의 zip()을 이용하면 쉽게 풀 수 있을 것 같음
deepcopy()까지 굳이 안써도 되는 이유는 원본 data list를 다시 이용하지 않기 때문에
그냥 data에 덮어 씌우면서 편하게 해주자

90도 돌릴 때 before(i,j) => after(i,j)로 바뀌면서 각 행마다 점화식이 생길 것 같은데
이걸 이용해서 '구현' 해줘도 풀릴 듯?

결과는 무조껀 nx3으로 나온다
'''
for t in range(int(input())):
    n = int(input())
    data = [input().split() for _ in range(n)]
    res = [[] for _ in range(n)]

    for _ in range(3):
        turn_data = []
        for i,temp in enumerate(zip(*data)):
            turn_data.append(list(reversed(temp)))
            res[i].append(''.join(list(reversed(temp))))
        data = turn_data
    ans = f'#{t+1}'
    print(ans)

    for row in res:
        print(*row)