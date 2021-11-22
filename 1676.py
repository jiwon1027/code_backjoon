n = int(input())
result = 1
for i in range(1,n+1):
	result = result* i
result = str(result)

result = result[::-1]
cnt = 0
for i in result:
	if i =='0':
		cnt+=1
	else:
		break
print(cnt)