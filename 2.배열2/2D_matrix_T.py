'''
3 3
1 2 3
4 5 6
7 8 9
'''

# input 1
#N, M = map(int,input().split())

#mylist = [0 for _ in range(N)]
# mylist = [0] * N

#for i in range(N):
#    mylist[i] = list(map(int,input().split()))

#print(mylist)


#input 2
#N, M = map(int,input().split())

#mylist = []

#for i in range(N):
#    mylist.append(list(map(int,input().split())))

#print(mylist)


# input 3
# N,M = map(int,input().split())
# mylist = [list(map(int,input().split())) for _ in range(N)]
# print(mylist)

# 0 initialize
# 주의: v = [[0]*3]*3 의 경우, 주소값을 복사해서 개별 할당이 일어나지 않음

#N = 3 # 행
#M = 4 # 열

#v = [[0 for _ in range(M)] for _ in range(N)]
# v = [[0]*M for_in range(N)]
#print(v)



## Transpose

#N,M = map(int,input().split())
#arr = [list(map(int,input().split())) for _ in range(N)]

#print(arr)

for i in range(N):
    for j in range(M):
        if i<j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)

# for i in range(N):
#     for j in range(i+1,M):
#         arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# print(arr)

