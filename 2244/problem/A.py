# A. Iskander and Drawings
import math

def solution(line):
    line_list = line.split('*')
    line_list.sort(reverse=True)
    answer = math.ceil(len(line_list[0])/2 )
    print(answer)


for t in range(int(input())):
    n = int(input())
    line = input()
    solution(line)