import sys

N = int(sys.stdin.readline().strip())
tree = {}
for i in range(N):
    p, l, r = sys.stdin.readline().strip().split()
    tree[p] = [l, r]

def preorder(p):
    if p != '.':
        print(p, end="")
        preorder(tree[p][0])
        preorder(tree[p][1])


def inorder(p):
    if p != '.':
        inorder(tree[p][0])
        print(p, end="")
        inorder(tree[p][1])


def postorder(p):
    if p != '.':
        postorder(tree[p][0])
        postorder(tree[p][1])
        print(p, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')