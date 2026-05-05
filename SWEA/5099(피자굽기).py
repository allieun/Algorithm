'''
문제 조건
    - 1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 꺼내는 순서는 달라질수 있음
    - 피자는 치즈가 모두 녹으면 화덕에서 꺼냄(치즈 값이 0이 되면 꺼냄)
    - 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 것이 목표
    - M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어듬 
    - 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어듬
    - 

활용 알고리즘 : 큐 시뮬레이션(완전한 bfs 스타일은 아니지만 큐 활용을 연습해보는 것)
'''
from collections import deque

def pizza():
    q = deque()
    for i in range(n):
        q.append([i+1, cheese[i]])
    
    next_idx = n
    while len(q) > 1:
        pizza_num, c = q.popleft()
        c //= 2

        if c == 0:
            if next_idx < m:
                q.append([next_idx + 1, cheese[next_idx]])
                next_idx +=1
        else:
            q.append([pizza_num, c])
    return q[0][0]

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    cheese = list(map(int, input().split()))
    
    answer = pizza()

    print(f'#{tc} {answer}')