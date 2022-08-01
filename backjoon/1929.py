def isprime(m,n):
  n += 1
  prime = [1] * n
  for i in range(2,int(n**0.5)+1):
    if prime[i]:
      for j in range(2*i,n,i):
        prime[j] = 0
  for i in range(m,n):
    if i > 1 and prime[i] == 1:
      print(i)

a,b = map(int,input().split())
isprime(a,b)


