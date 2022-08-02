import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
cards_num = Counter(data)
cards = cards_num.most_common()
print(cards[0][0])

