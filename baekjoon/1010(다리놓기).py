'''
강의 서쪽에 N개의 사이트가 있고, 동쪽에는 M개의 사이트가 있을 때, 강의 서쪽과 동쪽을 가장 많이 연결할 수 있는 경우의 수를 구하라
(단, 연결할 때 겹치면 안된다)
수의 범위 : 0 < N <= M < 30

이 문제의 메인 로직 : 조합


'''
t = int(input())

table = [[0] * 31 for _ in range(31)]
for i in range(31):
    for j in range(i+1):
        if i == 0 or j == i:
            table[i][j] = 1
        else:
            table[i][j] = table[i-1][j-1] + table[i-1][j]

for _ in range(t):
    n, m = map(int, input().split())

    print(table[m][n])



