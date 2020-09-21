def selectionSort(a):
    # i: 0 ~ len(n) - 1
    for i in range(0, len(a) - 1):  # 0, 1, 2, 3, 마지막은 자동으로 최소값
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]


arr = [64, 25, 10, 22, 11]
selectionSort(arr)
print(arr)

# 작은 값

def select(list,k):
    for i in range(0,k):
        minIndex = i
        for j in range(i+1,len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]

arr = [64, 25, 10, 22, 11]
print(select(arr,3))

# 큰 값

def select(list,k):
    for i in range(0,k):
        max_index = i
        for j in range(i+1,len(list)):
            if list[max_index] < list[j]:   # 이 조건만 바꾸며 ㄴ됨
                max_index = j
        list[i], list[max_index] = list[max_index], list[i]
    return list[k-1]

arr = [64, 25, 10, 22, 11]
print(select(arr,2))