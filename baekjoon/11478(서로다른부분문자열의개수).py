'''
문자열 s에서 서로 다른 부분 문자열의 개수를 구하기

1. 리스트 사용 시 처리시간이 오래 걸리기 때문에 set을 사용한다.
'''

import sys
input = sys.stdin.readline

s = input().strip()
substring = set()

n = len(s)

for i in range(n):
    for j in range(i+1, n+1):
        substring.add(s[i:j])

print(len(substring))