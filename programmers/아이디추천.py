import sys

input = sys.stdin.readline


def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    for i in new_id:
        if i == '-' or i == '.' or ('a' <= i <= 'z') or ('0' <= i <= '9'):
            answer += i
    answer = answer.replace('..', '.')

    if answer[0] == '.':
        answer = answer[2:]

    if answer[-1] == '.':
        answer = answer[0:len(answer) - 1]

    if len(answer) == 0:
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[0:15]
    if answer[-1] == '.':
        answer = answer[0:len(answer) - 1]
    if len(answer) <= 2:
        while len(answer) == 3:
            answer += answer[-1]

    return answer


data = input()
print(solution(data))