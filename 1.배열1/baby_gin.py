num = 456789  # Baby Gin 확인할 6자리 수

c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:  # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue;  # i += 1을 하지 않기 위해서, 같은 게 6개 있을 수도 있음
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue # run 의 경우의 수가 2개 발생할 수 있음
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")