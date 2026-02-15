# 카운팅 정렬 이해해보기

array = [7, 2, 3, 5, 7, 1, 4, 6, 7, 5, 0, 1]    # 숫자가 들어있는 리스트 array 입력
counting = [0] * (max(array)+1)                 # 이렇게 하는 이유는 카운팅 하는 리스트에는 array에 속한 값들 중 종류가 같은 것은 중복할거기 때문
# counting의 길이는 array의 최곳값 7을 기준으로 1개를 더 더함 -> 이유는 리스트는 0부터 시작하기 때문

for num in array:
    counting[num] += 1               # array를 순환하며 counting 리스트에 num값을 가진 인자가 나올 때마다 counting 리스트의 해당 인덱스에 1씩 더함

for i in range(1, len(counting)):    # 범위 설정을 이렇게 하는 이유: 누적합 계산은 인덱스 counting[0] 부터 시작이 아니라 counting[1]부터 시작
    counting[i] += counting[i-1]


result = [0] * len(array)            # array의 요소들을 정렬해서 넣을 리스트 (오름차순으로)

for num in reversed(array):
    idx = counting[num]
    result[idx-1] = num
    counting[num] -= 1

print(result)
