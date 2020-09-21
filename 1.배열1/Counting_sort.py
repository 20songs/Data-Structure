def Counting_Sort(A, B, k): # k 는 최대값+1

# A [] -- 입력 배열(1 to k) :: Source
# B [] -- 정렬된 배열        :: Temp > 결과
# C [] -- 카운트 배열       ::

    C = [0] * k

    for i in range(0, len(B)):  # 카운팅
        C[A[i]] += 1

    for i in range(1, len(C)):  # 누적 = 할당될 값의 인덱스를 업데이트
        C[i] += C[i - 1]

    for i in range(len(B)-1, -1, -1):  # 소트
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B

a = [0, 4, 1, 3, 1, 2, 4, 1] # 소스
b = [0] * len(a)             # 결과 저장 배열

print(a)
print(b)
print(Counting_Sort(a,b,max(a)+1))

