'''
숫자 카드 N개를 가지고 있는 상황에서 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드가 몇 개인지 구하는 코드 작성
sys를 사용해서 처리속도 향상
'''

import sys
input  = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

count = {}           # 딕셔너리를 사용해 효율적인 카운트 진행
for n in n_list:
    count[n] = count.get(n, 0) +1     # get을 사용해 n을 찾고, 만약 n이 없다면 key 값을 0으로 설정. 그리고 그 값에 1을더함 

print(*(count.get(m,0) for m in m_list))   # 그리고 이 리스트에서 m_list의 m을 찾고 있다면 그것의 key 값을 가져와 리스트에 넣음. 없다면 0