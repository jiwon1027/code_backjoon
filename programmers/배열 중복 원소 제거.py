import sys

input = sys.stdin.readline


def solution(arr):
    answer = [0]
    for i in arr:
        if not answer[-1] == i:
            answer.append(i)

    return answer[1:]
def fun(arr):
    result = []
    result.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            result.append(arr[i])
    return result

data = list(input())
print(fun(data))
print(solution(data))