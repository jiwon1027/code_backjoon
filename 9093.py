n = int(input())

for _ in range(n):
    data = input().split()

    for x in range(len(data)):
        string = data[x]
        reversed_string = string[::-1]
        print(reversed_string, end=" ")
    print('')