'''
치킨을 받는 등수는 1등 부터 5등까지
각 참가자는 해결한 문제 개수와 패널티 총합의 정보를 제공
순위 결정 기준 1순위는 해결한 문제 갯수
             2순위는 패널티 총합이 더 작은 경우
5등의 경우 최소 1문제 이상 풀었음

정렬과 단순 구현을 하는 문제

'''

n = int(input())
prize_list = []
for _ in range(n):
    solve, penalty = map(int, input().split())
    prize_list.append([-solve, penalty])        # solve를 추가할 때 -solve로 추가하는 이유는 sort를 사용하기 위해서

prize_list.sort()

if n > 5:
    target_compare = prize_list[4][0]
    count = 0
    for i in range(5, n):
        if prize_list[i][0] == target_compare:
            count += 1
    print(count)
else:
    print(0)