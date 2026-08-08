# A. Riptide
def solution():
    l = list(map(int, input().split()))
    l.sort()
    print(min(l[1]-l[0],l[2]-l[1]))



for t in range(int(input())):
    solution()