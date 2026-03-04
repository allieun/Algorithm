'''
회문을 판별할 때 회문 판별 함수 반환값과 recursion 함수 호출 횟수 출력하기

1. 회문 판별하는 방법 : 문자열을 뒤집었을 때 원래 입력 받은 내용과 같다면 회문
2. count라는 변수를 두고 해당 변수를 함수 내부로 호출
'''

def recursion(s, l, r):                  # s = 입력받는 문장, l = 왼쪽 인덱스, r = 오른쪽 인덱스 
    global count
    count += 1
    # 문자열의 양쪽을 비교하면서 가운데까지 도달했으면 회문으로 판단
    if l >= r:                          # 왼쪽 끝과 오른쪽 끝부터 비교하며 오기 때문에 인덱스 값은 항상 r이 더 큼
        return 1                        # l == r (가운데 문자가 하나 남았음) or ㅣ > r (이미 인덱스 교차) 인 경우에는 회문 검사 완료로 1 반환
    elif s[l] != s[r]:                  # 왼쪽 인덱스 값과 오른쪽 인덱스 값이 같지 않다면 0 반환 (회문이 아니라는 의미)
            return 0
    else:                               # 회문이고 아직 탐색할 인덱스가 남았을 경우 1씩 더하고 빼서 인덱스 번호 이동 후 탐색 재개(재귀)
         return recursion(s, l+1, r-1)
    
def ispalindrome(sentence):             # 회문 판별 여부에 recursion 함수 활용해서 재귀함수를 시작하기 위한 함수
    # 왜냐하면 입력 받는 값이 문자열 하나밖에 없기 때문에
    return recursion(sentence, 0, len(sentence)-1)  #len(sentence)-1 하는 이유는 인덱스가 0 부터 시작하기 때문에 길이에서 1을 뻬야 하기 때문
    
t = int(input())

for _ in range(t):
    sentence = input()
    count = 0
    result = ispalindrome(sentence)
    print(result, count)