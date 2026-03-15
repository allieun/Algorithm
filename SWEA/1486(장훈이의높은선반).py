'''
높이가 B인 선반에 접근하기 위해 직원들이 인간탑을을 쌓는다.
인간탑의 높이는 참여한 점원들의 키의 합
알아내야 할 것은 인간탑을 만들 수 있는 여러가지 높이 중 가장 높이가 낮은 인간탑(B와 가장 가까운 높이)

-> DFS로 풀어보아라 (다른 방법으로는 dp나 비트마스크도 있음)
'''

def dfs(idx, total):
    global answer
    if total - b >= answer:
        return
    if total >= b:
        answer = min(answer, total-b)
        return
    if idx == n:
        return
    dfs(idx+1, total + heights[idx])
    dfs(idx+1, total)


t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))

    answer = float('inf')
    dfs(0, 0)

    print(f'#{tc} {answer}')