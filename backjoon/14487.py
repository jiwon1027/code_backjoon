n = int(input())
cost = list(map(int,input().split()))

max_value = max(cost)
result = 0
cost.remove(max_value) #O(n)

for i in cost:
    result += i
print(result)