# A. Zero Sum 
def solution(n):
    a = list(map(int,input().split()))
    sum_of_array = sum(a)
    half_of_sum_of_array = abs(sum_of_array)/2
    print('YES' if n%2==0 and abs(half_of_sum_of_array)%2==0 else 'NO')


for t in range(int(input())):
    n = int(input())
    solution(n)


