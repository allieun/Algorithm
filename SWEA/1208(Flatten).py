'''
가장 값이 큰 인덱스에서 하나를 빼서 가장 값이 작은 인덱스에 1추가 하는 작업을 n회 동안 반복
최고점과 최저점의 차이라 0 혹은 1이라면 덤프 중지
덤프 횟수 종료 후 최저점과 최고 점의 차이를 계산
덤프로 인해서 최고점과 최저점이 계속해서 변하게 됨 -> 최고값과 최저값의 인덱스를 계속해서 찾아서 덤핑을 반복해야 함
이전 풀이에선 for문을 쓰지 않고 풀었기 때문에 이번에는 for 문을 사용해서 풀어보는 것이 목표
'''

t = 10

for tc in range(1, t+1):
    n = int(input())
    heights = list(map(int, input().split()))

    for i in range(n):
        max_height = max(heights)
        min_height = min(heights)

        if max_height - min_height <= 1:
            break

        max_idx = heights.index(max_height)
        min_idx = heights.index(min_height)

        heights[max_idx] -= 1
        heights[min_idx] += 1

    answer = max(heights) - min(heights)
    print(f'#{tc} {answer}')