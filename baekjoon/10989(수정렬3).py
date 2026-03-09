'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬해보기

N의 범위는 1부터 10,000

'''

import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001

for _ in range(n):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)