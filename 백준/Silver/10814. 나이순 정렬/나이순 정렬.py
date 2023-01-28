import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

def sol(members):
    members.sort(key=lambda x: (x[0]))
    return members

if __name__ == '__main__':
    n = int(input())
    members = []
    for i in range(n):
        age, name = input().split()
        members.append((int(age), name))
        
    sol(members)
    
    for i in range(n):
        print(members[i][0], members[i][1])