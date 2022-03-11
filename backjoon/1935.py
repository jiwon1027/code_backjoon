n = int(input())
data = input()
stack = []
num_list = []
for _ in range(n):
    num_list.append(int(input()))

for i in data:
    if 'A' <= i <= 'Z':
        stack.append(num_list[ord(i)-ord('A')])

    else:
        str2 = stack.pop()
        str1 = stack.pop()
        #print(stack)
        #print(str2, str1)
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print('%.2f' % stack[0])