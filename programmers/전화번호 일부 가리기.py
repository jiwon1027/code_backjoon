import sys

input = sys.stdin.readline


def solution(phone_number):
    temp = phone_number[::-1]
    cnt = 0
    answer = ''

    for i in temp:
        if cnt < 4:
            answer += i
            cnt += 1
        else:
            answer += '*'
    return answer[::-1]


data = input()

print(solution(data))