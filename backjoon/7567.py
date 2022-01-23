data = list(map(str,input()))
if data[0] == '(':
    result = 10
    temp = '('
else:
    result = 10
    temp = ')'

for i in range(1,len(data)):
    if data[i] == temp:
        result += 5
    else:
        result += 10
        if temp == '(':
            temp = ')'
        else:
            temp = '('
print(result)