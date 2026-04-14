'''
남학생 : 스위치 번호가 받은 수의 배수일 경우 스위치의 상태 변경(끄던가 키던가)
여학생 : 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
        그 구간에 속한 스위치의 상태를 모두 바꿈(구간에 속한 스위치 개수는 항상 홀수)
'''

import sys

# 입력을 더 빠르게 받기 위한 설정
input = sys.stdin.readline

# 1. 초기 데이터 입력
n = int(input())
switches = [-1] + list(map(int, input().split()))

# 2. 학생별 로직 수행
for _ in range(int(input())):
    gender, num = map(int, input().split())
    
    if gender == 1: # 남학생
        for i in range(num, n + 1, num):
            switches[i] = 1 - switches[i]
            
    else: # 여학생
        switches[num] = 1 - switches[num]
        k = 1
        while 1 <= num - k and num + k <= n and switches[num - k] == switches[num + k]:
            switches[num - k] = 1 - switches[num - k]
            switches[num + k] = 1 - switches[num + k]
            k += 1

# 3. 결과 출력
for i in range(1, n + 1):
    print(switches[i], end=" ")
    if i % 20 == 0:
        print()