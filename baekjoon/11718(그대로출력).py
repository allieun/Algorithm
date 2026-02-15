'''
입력받은 그대로 출력하는 문제

몇 줄이 나오던 그대로 그냥 출력해야 하기 때문에 EOF Error가 걸릴 수 도 있음
따라서 try-except를 쓰거나 sys를 활용하는 두 가지 방법이 있음.

sys.stdin.readlines() : 입력한 데이터의 모든 줄을 한꺼번에 읽어서 리스트 형태로 반환
여기에 rstrip()을 붙여서 줄바꿈 문자까지 제거
'''


import sys 

s = sys.stdin.readlines()

for line in s:
    print(line.rstrip())