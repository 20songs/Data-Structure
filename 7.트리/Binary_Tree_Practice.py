'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(node):
    global cnt                 # 읽으려면 global 안써도 인식
    if node:
        print(node,end=" ")
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node:
        inorder(tree[node][0])
        print(node, end=" ")
        inorder(tree[node][1])

def postorder(node):
    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=" ")

V = int(input()) # 정점
E = V-1          # 간선
tree = [[0]*3 for _ in range(V+1)] # 14*3
tmp = list(map(int,input().split()))
cnt = 0
# tree 저장
for i in range(E):
    p, c = tmp[i*2], tmp[i*2+1]
    if tree[p][0] == 0:
        tree[p][0] = c # left
    else:
        tree[p][1] = c # right
    tree[c][2] = p     # parent

#for t in tree:
#    print(*t) # *은 내용만, 구분해서 잘라서 , 프린트

preorder(1)
print()
print(cnt)
inorder(1)
print()
postorder(1)
print()
