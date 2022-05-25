data = [(1,1),(1,2),(1,3),(1,4),(1,7),(1,8)]


from bisect import bisect_left

print(bisect_left(data,(1,6)))

