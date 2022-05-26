# find 연산
def find(target):
    '''
    #시간복잡도 O(V), 모든 노드를 다 확이하게 되어 비효율적임
    # 여기서는 루트 노드 를 찾아서 return만 시켜준건데
    if parent[target] != target:
        return find(parent[target])
    return target
    '''

    if parent[target] != target:
        # 경로 압축 최적화
        parent[target] = find(parent[target])
    return parent[target]

# union 연산
def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 루트 노드를 기준으로 합침
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0, 1, 2, 3, 4, 5]

print(find(1), find(2), find(3), find(4), find(5))
print(parent)

union(1, 5)
union(2, 4)
union(4, 3)
union(5, 4)

print(find(1), find(2), find(3), find(4), find(5))
print(parent)