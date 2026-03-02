'''
수빈이의 위치 n, 동생의 위치 k
수빈이의 이동 방식 : 걷기 / 순간이동
1) 걷기 : 1초 후 x -1 혹은 x + 1로 이동
2) 순간이동 : 1초 후 2x의 위치로 이동

수빈이가 동생을 찾는 가장 빠른 시간은 몇 초 후인지 찾아보기

bfs 방식을 활용해서 풀기(이동은 델타 네 방향 이동이 아니라 +1, -1, *2)
'''
from collections import deque
import sys
input = sys.stdin.readline
 
def bfs(n, k):                       # 입력받은 정보인 n(수빈위치), k(동생위치)를 bfs 함수에 입력
    q = deque([n])                   # 덱에 시작 위치인 수빈이의 위치를 입력
    max_lim = 100000                 # 최대영역을 설정하는 이유는 수빈이와 동생이 위치 범위가 10만까지라서
    visited = [-1] * (max_lim + 1)   # visited 이렇게 설정하는 이유는 인덱스가 0부터 시작하기 때문
    visited[n] = 0                   # 첫 시작은 0(방문처리)

    while q:                      # 큐 안에서
        current = q.popleft()     # 현재 위치 확인
        if current == k:          # 만약 현재 위치가 동생의 위치라면 현재 위치까지 이동하느라 생긴 시간 출력
            return visited[current]
        
        for next_node in (current-1, current+1, current*2):     # 이동 방향(-1, +1, *2)의 범위에서
            if 0 <= next_node <= max_lim and visited[next_node] == -1:   # 다음 이동할 칸이 이동 범위 안이고, 아직 방문하지 않았다면
                visited[next_node] = visited[current]+1         # 다음 방문 노드는 현재 위치를 방문한 시간에 1을 더함
                q.append(next_node)               # 큐에 현재 방문한 노드를 넣어서 다음 탐색 진행

    

n, k = map(int, input().split())
print(bfs(n, k))