def bisect_left(arr, value, begin, end):
    if begin >= end:
        return begin
    mid = begin + (end - begin) // 2
    if arr[mid] < value:
        return bisect_left(arr, value, mid + 1, end)
    else:
        return bisect_left(arr, value, begin, mid)

array = [0.1, 0.2, 0.2, 0.2, 0.3, 0.6, 0.8, 1]



target = 0.3
start = array[0]
end = array[-1]
print(start)
print(end)

from bisect import bisect_left
print(bisect_left(array,target))


