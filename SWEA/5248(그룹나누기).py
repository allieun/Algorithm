'''
1번 부터 n 번까지 출석 번호가 있고, m 장의 신청서가 제출되었을 경우, 전체 몇 개의 조가 완성되는가?
한 사람이 여러 종이를 제출했거나 여러 사람이 한 사람을 지목했을 경우에도 같은 조가 된다.

풀이 유형 : DFS or 유니온파인드 (익숙해지기 위해 유니온파인드 사용)
풀이 방법
- 인접 리스트 생성
'''
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    parent = [i for i in range(n+1)]

    for i in range(0, len(data), 2):
        a = data[i]
        b = data[i+1]
        union(a, b)

    group = set()

    for i in range(1, n+1):
        group.add(find(i))

    answer = len(group)
    print(f'#{tc} {answer}')