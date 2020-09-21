def seq_search(a,n,key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1

arr = [4,9,11,23,2,19,7]
key = 23
print(seq_search(arr,len(arr),key))

def seq_search2(a,n,key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key:
        return i
    else:
        return -1

brr = [1,2,3,4,5,18,19,20]
key = 12
print(seq_search2(brr,len(brr),key))
