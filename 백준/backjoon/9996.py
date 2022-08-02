n = int(input())
data = input()
idx = data.index('*')
frond = data[:idx]
len_frond = len(frond)
end = data[idx+1:]
len_end = len(end)

#print(frond,end)

for _ in range(n):
    temp = input()
    if len(temp) < len(data)-1:
        print('NE')
        continue
    if temp[:len_frond] == frond and temp[len(temp)-len_end:] == end:
        print('DA')
    else:
        print('NE')



