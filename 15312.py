alphabet = [3,2,1,2,3,3,2,3,3,2,2,1,2,2,1,2,2,2,1,2,1,1,1,2,2,1]
data = []
data_temp = []
str_temp = []
A = list(map(str,input()))
B = list(map(str,input()))

for x in range(len(A)):
    str_temp.append(A[x])
    str_temp.append(B[x])


for i in range((len(str_temp)-1)):
    temp = alphabet[ord(str_temp[i]) - 65] + alphabet[ord(str_temp[i+1]) - 65]
    temp2 = temp % 10
    data.append(temp2)


while True:
    if len(data) == 2:
        break
    for i in range(len(data)-1):
        data_temp.append((data[i] +data[i+1])%10)
    data = data_temp
    data_temp = []
print(str(data[0])+str(data[1]))