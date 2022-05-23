from bisect import bisect_left,bisect_right

a = [1,2,4,4,8]
x = 9

print(type(bisect_left(a,x)))
print(bisect_right(a,x))