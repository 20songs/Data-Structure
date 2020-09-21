'''
5 5
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1
'''
# input
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def isnotwall(x,y):
    if x >= 0 and x < 5 and y >= 0 and y < 5:
        return True
    return False

def calAbs(a,b):
    if a-b > 0:
        return a-b
    else:
        return b-a


# explore nearby

n = len(arr)
m = len(arr[0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

total = 0
sum_list = []
for x in range(n):
    for y in range(m):
        sum = 0
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if isnotwall(newx,newy) == True:
                sum += calAbs(arr[x][y],arr[newx][newy])
        sum_list.append(sum)
        total += sum
print(total,sum_list)