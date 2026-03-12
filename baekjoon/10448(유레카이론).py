'''
자연수 n에 대해 삼각수 Tn의 공식
Tn = n(n+1)/2

위 공식을 활용해서 자연수가 주어졌을 때, 그 정수가 정확히 3개의 삼각수의 합으로 표현될 수 있을까?

1. 삼각수의 공식을 활용해서 삼각수를 구함 (k의 범위는 1000이하)

'''

def check(k):
    for a in tri_num:
        for b in tri_num:
            for c in tri_num:
                if a + b + c == k:
                    return 1
    return 0


t = int(input())
tri_num = []
n= 1

while True:
    tn = n * (n+1) // 2
    if tn > 1000:
        break
    else:
        tri_num.append(tn)
    n += 1


for _ in range(t):
    k = int(input())
    answer = check(k)
    print(answer)
