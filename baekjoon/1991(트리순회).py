'''
이진트리를 입력 받아 전위순회, 중위순회, 후위순회 결과 출력하기

'''
import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

def dfs1(root):      #전위순회
    if root != '.':
        print(root, end='')
        dfs1(tree[root][0])
        dfs1(tree[root][1])

def dfs2(root):      #중위순회
    if root != '.':
        dfs2(tree[root][0])
        print(root, end='')
        dfs2(tree[root][1])


def dfs3(root):      #후위순회
    if root != '.':
        dfs3(tree[root][0])
        dfs3(tree[root][1])
        print(root, end='')

dfs1('A')
print()
dfs2('A')
print()
dfs3('A')