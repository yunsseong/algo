case = int(input())

def search(note1, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if note1[mid] == target:
            return 1
        elif note1[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for _ in range(case):
    note1_len = int(input())
    note1 = sorted(list(map(int, input().split())))
    input()
    note2 = list(map(int, input().split()))
    for i in note2:
        print(search(note1, i, 0, note1_len-1))

