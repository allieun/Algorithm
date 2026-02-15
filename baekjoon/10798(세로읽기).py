'''
칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

5줄이 입력됨, 각 줄의 길이는 다름.

총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다.
'''

grid = [list([-1]*15) for _ in range(5)]

answer = []

for r in range(5):
    line = input()
    for c in range(len(line)):
        grid[r][c] = line[c]

for c in range(15):
    for r in range(5):
        if grid[r][c] != -1:
            answer.append(grid[r][c])

print(*answer, sep='')