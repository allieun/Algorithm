'''
최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).

풀이 방법: 카운팅 정렬을 활용해서 풀면 될 거 같다고 생각

1. 입력 숫자의 빈도수를 체크할 카운팅 리스트 생성
2. 카운트 리스트의 인덱스 값에 해당하는 수가 리스트에서 확인될 때마다 해당 인덱스 값에 1씩 추가
3. 카운트 리스트를 거꾸로 순회하며 최빈수를 찾는다.
4. 카운트 리스트를 역순회 하는 이유는 최빈수가 여러개라면 그 중 가장 큰 수를 출력해야 하기 때문에
5. 가장 큰 수를 최빈수로 찾으면 바로 break

'''

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    # 숫자들의 입력 빈도를 체크할 카운팅 전용 리스트 생성
    count = [0]*(max(numbers)+1) # 인덱스가 0 부터 시작하기 때문에 +1을 해줌

    for number in numbers:
        count[number] += 1       # 키운팅 리스트의 해당 인덱스 수와 같은 값이 나올 때 마다 해당 인덱스에 1씩 더함

    max_num = max(count)

    for i in range(len(count)-1, -1, -1):
        if count[i] == max_num:
            answer = i
            break
        answer = count.index(max(count))

    print(f'#{tc} {answer}')