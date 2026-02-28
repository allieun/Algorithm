'''
N x N 의 배열에서 M x M 크기의 파리채로 파리를 잡을 때, 가장 많이 잡힌 파리의 개수 구하기
(델타 같겠지만 이중 반복문으로 푸는 문제)

1. n x n 범위의 배열을 입력 받음
2. 최대로 잡는 파리의 개수를 지정할 변수를 설정
3. 탐색할 기준점을 설정(왼쪽 상단 모서리를 기준점으로 설정)
4. m x m 범위의 파리채에서 해당 범위안의 값들을 합한 값을 현재 잡은 파리 마리수로 지정
5. 현재 잡은 마리 수와 최대 값 변수를 비교해서 더 큰 변수를 최대 값 변수로 설정
6. 그렇게 가장 큰 값을 정답으로 출력
'''

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    max_catch = 0

    for gr in range(n-m+1):                      # 파리채 범위 설정의 기준점의 좌표 gr, gc
        for gc in range(n-m+1):
            catch = 0                            # 현재 m x m 범위의 파리채에서 잡은 파리의 합
            for r in range(gr, gr+m):
                for c in range(gc,gc+m):         # 파리채 범위 (gr에서부터 m칸까지의 범위)에서 
                    catch += grid[r][c]          # 현재 잡은 파리의 개수를 합 변수에 추가

            if catch > max_catch:                # 현재 잡은 마리수와 최대 마리수를 비교해 더 큰 쪽을 최대 마리수로 변경
                max_catch = catch
    
    print(f'#{tc} {max_catch}')