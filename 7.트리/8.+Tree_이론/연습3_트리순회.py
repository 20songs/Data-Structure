'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(node):
    if node != 0:
        print(node, end=" ")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != 0:
        inorder(tree[node][0])
        print(node, end=" ")
        inorder(tree[node][1])

def postorder(node):
    if node != 0:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=" ")

def printTree():
    for i in range(1, V+1):
        print("%2d | %2d %2d %2d" % (i, tree[i][0], tree[i][1], tree[i][2]))

# --------------------------------------------------------------------------
V = int(input())    # 정점수
E = V - 1           # 간선수
tree = [[0 for _ in range(3)] for _ in range(V+1)]  #left, right, parent
temp = list(map(int, input().split()))

for i in range(E):
    n1 = temp[i * 2]
    n2 = temp[i * 2 + 1]
    if not tree[n1][0]:
        tree[n1][0] = n2   # left
    else:
        tree[n1][1] = n2   # right
    tree[n2][2] = n1       # parent

printTree()
# for t in tree:
#     print(*t)

print("전위순회 : ", end = "")
preorder(1)
print()

print("중위순회 : ", end = "")
inorder(1)
print()

print("후위순회 : ", end = "")
postorder(1)
print()
