a = 'ABCD'
b = '1234'

new_str1 = ''
new_str2 = ''

for i in range(len(a)):
    new_str1 += a[i]+b[i]
for i in range(len(a)):
    new_str2 += a[i]+b[-i-1]
print(new_str1)
print(new_str2)


