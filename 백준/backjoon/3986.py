n = int(input())
res = 0
for _ in range(n):
    stack = []
    word = input()
    stack.append(word[0])
    #print(stack)

    for i in word[1:]:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    if not len(stack):
        res += 1
print(res)


