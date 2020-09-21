T = int(input())

for t in range(1,T+1):
    n = int(input())

    snail = [[0 for _ in range(n)] for _ in range(n)]
    rows = len(snail)
    cols = len(snail[0])

    dr = [0,1,0,-1]
    dc = [1,0,-1,0]

    r = 0
    c = 0
    num = 1
    while c!= n-1:
        r += dr[0]
        c += dc[0]
        snail[r][c] = num
        num += 1
    while r!= n-1:
        r += dr[1]
        c += dr[1]
        snail[r][c] = num
        num += 1
    while r!=0:
        r += dr[2]
        c += dr[2]
        snail[r][c] = num
        num += 1
    while
    print(snail)


