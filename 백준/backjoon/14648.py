n,q = map(int,input().split())
seq = list(map(int,input().split()))
query = [list(map(int,input().split())) for _ in range(q)]

for row in query:
    result = 0
    if row[0] == 1:
        for j in range(row[1],row[2]+1):
            result += seq[j-1]
        seq[row[1]-1], seq[row[2]-1] = seq[row[2]-1], seq[row[1]-1]
    else:
        temp = 0
        temp1 = 0
        for a in range(row[1],row[2]+1):
            temp += seq[a-1]
        for b in range(row[3],row[4]+1):
            temp1 += seq[b-1]

        result = temp - temp1
    print(result)
