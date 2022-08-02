n = int(input())

for _ in range(n):
    k = int(input())

    for j in range(k):
        for i in range(k):
            if j == 0 or j == (k-1):
                print('#',end='')
            else:
                if i == 0 or i == (k-1):
                    print('#', end='')
                else:
                    print('J',end='')
        print('')
    print('')