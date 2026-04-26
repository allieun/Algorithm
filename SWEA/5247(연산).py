'''
사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 할까?
연산의 중간 결과도 항상 백만 이하의 자연수여야 한다(= 연산 값이 음수가 되면 고려 자체 X)
-> 항상 각 노드에 대한 가지수는 4가지 (연산 가능 경우의 수 4대)

결론적으로는 최단경로를 찾는 문제와 같기 때문에 BFS로 풀어야 하는 문제

'''
from collections import deque

def bfs(start, goal):
    q = deque([(start, 0)])     # 현재 위지와 이동 거리(시작 시에는 이동한 적이 없으므로 0)
    visited = [False] * 1000001     # m의 최대범위가 1,000,000이기 때문에
    visited[start] = True       # 시작하는 위치는 방문처리
    while q:
        current, dist = q.popleft()
        if current == goal:     # 현재 위치가 목표 위치일 경우 거리 배수 반환
            return dist
        for next_node in [current+1, current-1, current*2, current-10]:     # 4가지 연산에 대한 결과값 중에서
            if 0 <= next_node < 1000000 and not visited[next_node]:     # 범위 안에 있고, 방문한 적이 없다면
                q.append((next_node,dist+1))        # 큐에 넣어 다음 탐색 진행

t = int(input())

for tc in range(1, t+1):
    n, m= map(int, input().split())     # n = 시작점, m = 목표점
    answer = bfs(n, m)
    print(f'#{tc} {answer}'