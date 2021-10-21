data = input()
n1, n2, n3 = list(map(int, data))


def max3(n1, n2, n3):
    Max = max(n1, n2, n3)

    return Max


def min3(n1, n2, n3):
    Min = min(n1, n2, n3)

    return Min


max = max3(n1, n2, n3)
min = min3(n1, n2, n3)
print("가장큰수 :", max)
print("가장작은수 :", min)