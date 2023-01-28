import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x=0):
        self.stack.append(x)
    
    def pop(self):
        if self.size() == 0:
            return -1
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.size() == 0:
            return -1
        return self.stack[-1]

if __name__ == '__main__':
    n = int(input())
    s = MyStack()
    for i in range(n):
        command = []
        command = input().split()
        if command[0] == 'push':
            s.push(command[1])
        elif command[0] == 'pop':
            print(s.pop())
        elif command[0] == 'size':
            print(s.size())
        elif command[0] == 'empty':
            print(s.empty())
        elif command[0] == 'top':
            print(s.top())