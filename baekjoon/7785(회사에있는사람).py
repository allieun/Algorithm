'''
로그가 주어졌을 때 현재 회사에 어떤 사람이 있는지 모두 구하는 코드 작성

첫번째: n(로그에 기록된 출입 기록 수)
두번째 : n개의 줄에 출입기록이 순서대로 주어짐 (이름 + enter / leave)

** 작성해본 코드 **
n = int(input())
here = []

for _ in range(n):
    name, status = input().split()
    if status == 'enter':
        here.add(name)
    elif status == 'leave':
        here.discard(name)
result = sorted(here, reverse=True)

print('\n'.join(here))
'''
# 위 코드 처럼 풀면 로컬에서는 잘 돌아가지만 백준에서는 오답처리 됨 (일단 처리속도부터 너무 느림)
import sys
input = sys.stdin.readline                  # sys를 써서 처리 속도 향상

n = int(input())
here = set()                                # 리스트 대신 set 사용

for _ in range(n):
    name, status = input().split()          # 이름과 출입기록을 공백을 두고 받는다
    if status == 'enter':                   # 출입기록이 enter이면 셋에 추가
        here.add(name)
    elif status == 'leave':                 # 출입기록이 leave면 set에서 제거(더 안전하게 discard 사용)
        here.discard(name)

result = sorted(here, reverse=True)        # set은 순서가 없기 때문에 sorted를 사용해 리스트로 바꿔준 뒤 reverse=True로 역순으로 배치

print('\n'.join(result))