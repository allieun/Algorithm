'''
n = 이동해야 하는 정류장의 끝 번호
k = 한 번에 최대 이동할 수 있는 정류장 수
m = 충전기가 설치되어있는 정류장 수

전체 정류장 n의 범위에서 range(n+1) -> range(10)일 경우 마지막이 9이기 때문
현재 위치는 0에서 시작 -> k까지 이동하는데(+k), 만약 그 자리에 충전소가 있다면 현재위치를 +k로 업데이트
만약 그 위치에 충전소가 없다면 -1씩 하며 충전소 인덱스를 찾음

나는 부분수열에서도 썼었던 투포인트 그리디 알고리즘 방식을 활용하고 싶음

'''

t = int(input())

for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    station = list(map(int, input().split()))

    current = 0    # 현재 버스 위치
    charge = 0     # 충전 횟수
                                                  # range(start, stop, step)인데 step이 -1이므로 k 부터 stop +1까지만 순회
    while current + k < n:
        for move in range(k, 0, -1):              # move = 버스가 실제로 이동할 거리 k의 범위 안에서 역 순으로 이동
            if (current+move) in station:         # 현재위치 + 실제 이동할 거리의 값이 station 리스트에 포함된다면
                current += move                   # 버스의 위치는 현재 위치 + 실제 이동할 거리
                charge += 1                       # 충전 횟수에 1 추가
                break
        else:
            charge = 0
            break
    print(f'#{tc} {charge}')
