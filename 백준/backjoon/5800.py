k = int(input())
for c in range(1,k+1):
    temp = list(map(int, input().split()))
    grade = temp[1:]
    grade.sort()
    gap = -1
    for i in range(len(grade)-1):
        if grade[i+1] - grade[i] >= gap:
            gap = grade[i+1] - grade[i]
    print(f'Class {c}')
    print(f'Max {grade[-1]}, Min {grade[0]}, Largest gap {gap}')
