'''
9 x 9 배열의 격자판이 주어지고, 그 격자판 안에 각각의 81개를  9x9 배열로 입력받음
이 격자판 안에서 최댓값을 찾고, 그 인덱스까지 표기하기

완전탐색 연습 문제

1. 최댓값 변수를일단 -1로 시작 (그 이유는 0도 있을 수 있기 때문에 고려대상에 포함되어야 함)
2. 격자판의 (0, 0) 부터 (8, 8)까지 전부 순회하며 최댓값 변수와 비교 -> 더 크다면 그 값을 최댓값으로
3. 최댓값의 위치까지 표시해야 하기 때문에 행 인덱스 값과열 인덱스 값에 1을 더함 (왜냐하면 문제는 0부터가 아니라 인엑스가 1부터 시작)
4. 각각의 값을 출력
'''



grid = [list(map(int, input().split())) for _ in range(9)]

max_num = 0

for i in range(9):
    for j in range(9):
        if grid[i][j] > max_num:
            max_num = grid[i][j]
            max_row = i + 1
            max_column = j + 1 

print(max_num)
print(max_row, max_column)