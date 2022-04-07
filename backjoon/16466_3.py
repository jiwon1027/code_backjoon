global arr

def func():
    answer = 1
    for i in arr:
        if i == answer:
            answer += 1
    return answer

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

print(func())