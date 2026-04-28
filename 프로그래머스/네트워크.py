'''
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
네트워크의 개수를 return 하도록 solution 함수를 작성

인풋 방식 예시 : [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

문제 풀이 알고리즘 : DFS (깊이 탐색 방법)

프로그래머스는 이미 입력값이 매개변수로 들어오는 방식을 취하기 때문에 def solution 안에서 다 이루어져야 함

'''

def solution(n, computers):
    answer = 0
    visited = [0] * n

    def dfs(current):
        visited[current] = 1
        for next_node in range(n):
            if computers[current][next_node] == 1 and not visited[next_node]:
                dfs(next_node)


    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(1)

    return answer
