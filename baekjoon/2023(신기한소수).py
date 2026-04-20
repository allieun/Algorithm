'''
왼쪽부터 끝자리까지의 모든 자리수가 소수인 n자리 수를 출력한다?

문제 유형 : DFS

'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def dfs(num, length):
    if length == n:
        print(num)
        return
    for i in [1, 3, 5, 7, 9]:
        new_num = num * 10 + i
        if is_prime(new_num):
            dfs(new_num, length+1)



n = int(input())

for start in [2, 3, 5, 7]:
    dfs(start, 1)