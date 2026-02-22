'''
첫번째 : n과 m을 입력받음
두번째 : n줄만큼 포켓몬 이름을 입력받음
세번쨰 : m줄만큼 찾고자 하는 포켓몬 이름 또는 숫자를 입력받음
네번째 : 이름이라면 포켓몬이 몇 번째로 입력되었는지, 숫자라면 그 숫자번째에 입력된 이름이 무엇인지 출력

리스트와 딕셔너리 두 개 다 사용해 문제 풀기.
역시 sys를 사용해 처리속도 향상시키기
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poke_list = []
poke_dict = {}

for i in range(n):
    name = input().strip()            # n 줄 만큼 이름 입력받기
    poke_list.append(name)            # 리스트에 이름들 추가
    poke_dict[name] = i+1             # 딕셔너리에도 이름 추가하며, 벨류값은 i+1로 줌(왜냐하면 인덱스가 0부터 주어지기 때문)

for j in range(m):
    search = input().strip()
    if search.isdigit():             # 입력받은 내용이 숫자라면
        idx = int(search)            # 숫자로 변환해서 1을 뺀 위치의 리스트 값을 출력(리스트도 0부터 시작)
        print(poke_list[idx-1])
    else:
        print(poke_dict[search])    # 숫자가 아니라면 딕셔너리에서 그 이름에 해당하는 벨류값 출력