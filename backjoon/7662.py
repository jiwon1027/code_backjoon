t = int(input())
for _ in range(t):
    k = int(input())
    command, num = input().split()
    data = []

    if command == 'I':
        data.append(num)

    if command == 'D' and num == '1':

        print('최대삭제')

    if command == 'D' and num == '-1':
        print('최소삭제')








