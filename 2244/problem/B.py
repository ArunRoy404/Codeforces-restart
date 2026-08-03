# B. Nikita and Books
def solution():
    n = int(input())
    a = list(map(int, input().split()))

    prev_num = 0
    carry = 0

    for i in range(n):
        num = a[i]
        current_num = num + carry
        new_num = prev_num + 1
        leftover_num = current_num - new_num


        if prev_num >= new_num or leftover_num<0:
            print("NO")
            return

        prev_num = new_num
        carry = leftover_num
        # print(prev_num, end=' ')
    print("Yes")


for t in range(int(input())):
    solution()
