'''
단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력
find()를 활용해서 문제를 해결하면 좋을 것 같다. (이전까지는 잘 안써오기는 했어 사용 방법 다시 배움)

1. 알파벳을 그냥 하나의 스트링으로 받음: a 부터 z 까지
2. 알파벳이라는 스트링에 word가 있는지 find()를 사용해 찾음.
3. 그 다음 공백 없이 출력

'''



word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for char in alphabet:
    print(word.find(char), end=' ')