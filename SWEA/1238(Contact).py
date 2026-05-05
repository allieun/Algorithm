'''
문제 조건
    - 비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때, 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수
    - 방향이 있는 일방향 그래프
    - 연락 번호는 최대 1 이상 100이하

활용할 알고리즘 : BFS (연락이 단계 별로 진행되며, 마지막 레벨이 어디인지 정확히 확인 가능)
'''
from collections import deque

def bfs(start):
    q = deque([start])
    visited[start] = True
    answer = start                 # 초기 정답값(만약 시작점에서 연결된게 없다면 그냥 start 노드로 끝)

    while q:
        size = len(q)     # 현재 연락 단계에 있는 사람의 수 (1에서 2, 3, 그렇다면 2에서는 4, 3에서는 7 이런 식으로 단계가 있음)
        max_num = 0         # 사이즈를 미리 지정해두면 그 단계에서는 연결된 노드까지만 처리
        for _ in range(size):           # 목표 : 가장 마지막에 연락받은 사람 중 번호가 가장 큰 사람
            curr = q.popleft()
            max_num = max(max_num, curr)    # max_num = 현재 단계에서 연락 받는 사람 중 가장 번호가 큰 사람 지정 변수
            for next_node in graph[curr]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
        answer = max_num
    return answer       # 큐 안에서 answer를 계속해서 갱신하기 때문에 최종 asnwer = 마지막 단계의 최대 번호


t = 10

for tc in range(1, t+1):
    length, start = map(int, input().split())
    contact = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    visited = [False] * 101

    for i in range(0, length, 2):
        a = contact[i]
        b = contact[i+1]
        graph[a].append(b)

    answer = bfs(start)

    print(f'#{tc} {answer}')