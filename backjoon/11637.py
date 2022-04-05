t = int(input())

for _ in range(t):
    n = int(input())
    candi = []
    for _ in range(n):
        candi.append(int(input()))

    votes = sum(candi) // 2
    max_votes = max(candi)

    if candi.count(max_votes) > 1:
        print('no winner')
    else:
        if max_votes > votes:
            print('majority winner',candi.index(max_votes) + 1)
        else:
            print('minority winner',candi.index(max_votes) + 1)