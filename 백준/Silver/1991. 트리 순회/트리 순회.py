import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

pre_list = []
in_list = []
post_list = []


def preorder(r):
    if r != '.':
        pre_list.append(r)
        preorder(tree[r][0])
        preorder(tree[r][1])


def inorder(r):
    if r != '.':
        inorder(tree[r][0])
        in_list.append(r)
        inorder(tree[r][1])


def postorder(r):
    if r != '.':
        postorder(tree[r][0])
        postorder(tree[r][1])
        post_list.append(r)


preorder('A')
inorder('A')
postorder('A')

print(''.join(pre_list))
print(''.join(in_list))
print(''.join(post_list))