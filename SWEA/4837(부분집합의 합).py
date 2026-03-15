'''
1부터 12까지의 숫자를 원소로 가진 집합 A
A의 부분집합 중 n개의 원소를 가지고 있고, 그 원소의 합이 k인 부분집합의 개수 구하기

N의 범위가 1부터 12까지 이기 때문에 완전탐색으로 풀면 된다 (DFS)

'''
def dfs(idx, count, total):
    global answer                       # 경우의 수를 확인할 변수 값을 global로 호출
    if count > n or total > k:         # 부분집합에 포함된 수가 n개 초과하거나 그 원소들의 합이 k를 초과할 경우 그냥 통과
        return
    if idx == 13:                       # 1부터 12까지 다 돌았을 때 (13은 범위에 포함되지 않아서 탐색 종료)
        if count == n and total == k:       # n개 만큼 부분집합에 넣었고, 그 원소들의 합이 k인 경우
            answer += 1                 # 조건을 만족하는 경우의 수 1 추가
        return                          

    dfs(idx+1, count+1, total+idx)      # 현재 숫자(idx)를 포함하는 경우
    dfs(idx+1, count, total)            # 현재 숫자(idx)를 포함하지 않는 경우


t = int(input())

for tc in range(1, t+1):
    n, k = map(int, input().split())

    answer = 0                          # 가능한 경우의 수를 확인할 변수

    dfs(1, 0, 0)                        # idx가 1부터 시작하는 이유는 N의 범위가 1부터 12까지이기 때문
    print(f'#{tc} {answer}')