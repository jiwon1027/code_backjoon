import sys

input = sys.stdin.readline


def solution(phone_number):
    temp = phone_number[::-1]
    cnt = 0
    answer = ''
    print(temp)

    for i in temp:
        if cnt <= 4:
            answer += '*'
            cnt += 1
        else:
            answer += i
        print(answer)
    return answer


data = input()

print(solution(data))
