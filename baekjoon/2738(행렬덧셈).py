'''
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 코드 작성해보기.
'''


n, m = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(n)]       # n x n 배열 리스트
B = [list(map(int, input().split())) for _ in range(m)]       # m x m 배열 리스트

for i in range(n): 
    sum = []                                                  # 합계를 넣을 빈 리스트를 생성
    for j in range(m):
        sum_value = A[i][j] + B[i][j]
        sum.append(sum_value)

    print(*sum)                                                # 결과값을 그냥 출력하면 리스트로 나오기 때문에 언패킹을 한 뒤 출력