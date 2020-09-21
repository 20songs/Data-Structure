def BubbleSort(a): # 정렬할 List = range(4,0,-1), len(a)=5
    for i in range(len(a)-1) : # 범위의 끝 위치
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] # swap

data = [55,7,78,12,42]
BubbleSort(data)
print(data)