n = int(input())
count = 1
stack = []
result = []
no_message=True

for i in range(n):
    x = int(input())

    while count <= x:
      stack.append(count)
      result.append("+")
      count += 1


    if stack[-1]==x:
        stack.pop()
        result.append("-")
    else:
        no_message = False

if no_message==False:
    print("NO")
else:
    print("\n".join(result))