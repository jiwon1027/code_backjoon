data = input()

for i in range(len(data)):
    if i != 0 and i % 10 == 0:
        print()
    print(data[i], end='')
