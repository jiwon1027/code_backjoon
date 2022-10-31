

def solution(registered_list, new_id):

    registered_list = set(registered_list)

    while True:
        if not new_id in registered_list:
            return new_id
        else:
            idx = -1
            for i, v in enumerate(new_id):
                if "0" <= v <= "9":
                    idx = i
                    break
            if idx == -1:
                idx = len(new_id)

            S = new_id[:idx]
            N = new_id[idx:]
            # print(S)
            # print(N)

            N_number = 0
            if not len(N) == 0:
                N_number = int(N)

            N_number += 1

            N1 = str(N_number)

            new_id = S + N1




registered_list = ["apple1", "orange", "banana3"]
new_id = "apple"


print(solution(registered_list, new_id))