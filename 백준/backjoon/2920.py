data = list(map(int,input().split()))
temp = list(range(1,9))

if data == temp:
    print('ascending')
elif data == temp[::-1]:
    print('descending')
else:
    print('mixed')