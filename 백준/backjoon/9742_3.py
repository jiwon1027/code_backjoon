from itertools import permutations

def permutation(depth):
    global cnt

    if depth == len(data):
        print(*isSelected)
        return

    for i in range(len(data)):
        if not visited[i]:
            isSelected[depth] = data[i]
            visited[i] = 1
            permutation(depth+1)
            visited[i] = 0


from math import factorial

while True:
    try:
        data, n = input().split()
        n = int(n)

        if n > factorial(len(data)):
            print('No permutation')
        else:
            #순열 스따또
            #nPn
            cnt = 0

            permu_data = permutations(data)

            for permu in permu_data:
                cnt+=1
                if cnt == n:
                    print(*permu)
                    break


            visited = [0] * len(data)
            isSelected = [0] * len(data)
            #permutation(0)
    except:
        break
