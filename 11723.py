import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
s = 0

for _ in range(n):
    tmp = input().rstrip().split()
    if len(tmp) == 2:
        order, num = tmp[0], int(tmp[1])
    else:
        order, num = tmp[0], 0

    if order == "add":
        s |= (1 << num)

    elif order == "remove":
        s &= ~(1 << num)

    elif order == "check":
        if s & (1 << num):
            print("1\n")
        else:
            print("0\n")

    elif order == "toggle":
        s ^= (1 << num)

    elif order == "all":
        s = (1 << 21) - 1

    elif order == "empty":
        s = 0


