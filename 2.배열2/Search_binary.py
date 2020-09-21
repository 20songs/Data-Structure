
def binarySearch(a, key):
    start = 0
    end = len(a)-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key: # 검색 성공
            return middle
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1 # 검색 실패

arr = [2,4,7,9,11,19,23]
key = 7
print(binarySearch(arr,key))
key = 20
print(binarySearch(arr,key))

def self_binary(a,low,high,key):
    if low>high:
        return False
    else:
        middle = (low+high)//2
        if key == a[middle]:
            return middle
        elif key > a[middle]:
            self_binary(a,low,middle-1,key)
        elif key < a[middle]:
            self_binary(a,middle+1,high,key)

key = 7
print(self_binary(arr,0,len(arr),key))