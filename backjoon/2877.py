k = int(input())
base_2 = format(k+1, 'b')
base_2 = base_2[1:]

print(base_2.replace('0', '4').replace('1', '7'))
