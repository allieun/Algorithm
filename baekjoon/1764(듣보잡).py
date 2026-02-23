'''
들어 보지 못한 사람의 수 : n
본 적 없는 사람의 수 : m
n개의 줄에 들어보지 못한 사람의 이름 입력
n+2번쨰 줄 부터 보지도 못한 사람의 이름 주어짐

둘 모두에 해당하는 사람의 수와 이름을 순서대로 출력(한 줄에 하나씩)
'''

import sys
input = sys.stdin.readline               # sys를 사용해 처리속도 향상

n, m = map(int, input().split())

no_hear = set()                         # 리스트말고 셋으로 받아서 처리속도 향상
for _ in range(n):
    no_hear.add(input().strip())        # add를 사용해 차례대로 셋에 추가

result = []                             # 결과값을 담을 빈 리스트
for _ in range(m):
    no_see = input().strip()            # 보지도 못한 인원 차례대로 입력받음
    if no_see in no_hear:               # 보지도 못한 사람의 이름이 듣지도 못한 사람 셋에 있으면
        result.append(no_see)           # 그 이름을 결과값 리스트에 추가한다,
result.sort()                           # 결과값 리스트를 정렬한다
print(len(result))                      # 겹친 사람 몇명인지, 긜고 그 이름이 누구인지를 join을 통한 줄바꿈으로 표현
print('\n'.join(result))
