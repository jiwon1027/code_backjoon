arr = [1,2,3,4,5,6]



def solution(arr):
    res = []
    def fun(arr,res):
        if len(arr) == 1:
            print(arr)
            res += arr
            return
        else:
            arr = arr[::-1]

            if len(arr) % 2 == 0:
                temp1 = arr[:len(arr) // 2]
                temp2 = arr[(len(arr) // 2):]

                fun(temp1,res)
                fun(temp2,res)

            else:
                temp1 = arr[:(len(arr) // 2) + 1]
                temp2 = arr[(len(arr) // 2) + 1:]
                fun(temp1,res)
                fun(temp2,res)

    fun(arr,res)
    return res
print(solution(arr))
