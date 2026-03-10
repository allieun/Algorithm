'''
숫자와 콤마로만 이루어진 문자열 s에서 자연수만의 합을 구해보자
s의 첫 문자와 마지막 문자는 항상 숫자이며 콤마는 연속으로 주어지지 않음

1. 일단 문자열 전체를 입력 받음 (sys.stdin.read() 사용)
2. 줄 바꿈을 없애고 하나로 합친다
3. 합친 목록에서 쉼표를 제거한다
4. 
'''
import sys

s = sys.stdin.read()
whole = s.replace('\n', '')         # 줄바꿈 제거
numbers = list(map(int, whole.split(',')))      # 리스트로 감싸면서 쉼표(,)로 분리

answer = sum(numbers)
print(answer)