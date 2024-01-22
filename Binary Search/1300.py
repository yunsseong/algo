n = int(input())
k = int(input())

def cal(num):
    if num != 1 and num !=n:
        return 2

    if num == 1 or num == n**2:
        return 1

    if num == n:
        return 3


cnt = 0
inc = 1
while cnt < k:
    cnt += cal(inc)
    inc += 1

print(cnt)