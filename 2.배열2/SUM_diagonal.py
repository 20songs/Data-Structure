for _ in range(1,11):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]

    rows = len(matrix)
    cols = len(matrix[0])

    max_val = 0
    for x in range(rows):
        sum_r = 0
        sum_c = 0
        sum_d = 0
        for y in range(cols):
            sum_r += matrix[x][y]
            sum_c += matrix[y][x]
            if x == y or x+y == 4:
                sum_d += matrix[x][y]
        if sum_r > sum_c and sum_r > max_val and sum_r > sum_d:
            max_val = sum_r
        elif sum_c > sum_r and sum_c > max_val and sum_c > sum_d:
            max_val = sum_c
        elif sum_d > sum_r and sum_d > sum_c and sum_d > max_val:
            max_val = sum_d

    print(f'#{n}',max_val)