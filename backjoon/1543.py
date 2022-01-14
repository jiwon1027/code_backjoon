data = input()
part = input()

print(data.count(part))

'''
#count 없이 풀기(슬라이싱 이용)
data = input()
part = input()
n=0
cnt = 0
while n <= len(data) - len(part):
    if data[n:n+len(part)] == part:
        cnt += 1
        n += len(part)
    else:
        n += 1
print(cnt)
'''