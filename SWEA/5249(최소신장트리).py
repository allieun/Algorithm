'''
0번부터 V번까지의 노드와 E개의 간선을 가진 그래프
최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 것이 목표

풀이 유형 : 유니온 파인드 + 크루스칼

크루스칼의 핵심 : 가중치가 작은 간선부터 확인하는 것

'''
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)
    if root_a == root_b:
        return False
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
    return True


t = int(input())

for tc in range(1, t+1):
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))
    edges.sort()

    parent = [i for i in range(v+1)]
    result = 0
    count = 0

    for w, n1, n2 in edges:
        if union(n1, n2):
            result += w
            count += 1
            if count == v:
                break

    print(f'#{tc} {result}')