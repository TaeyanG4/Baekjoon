import sys
input = sys.stdin.readline
import math
from collections import *
from itertools import *

class MyDeque:
    def __init__(self):
        self.queue = deque()

    def push_front(self, x=0):
        self.queue.appendleft(x)
        
    def push_back(self, x=0):
        self.queue.append(x)
    
    def pop_front(self):
        if self.size() == 0:
            return -1
        return self.queue.popleft()
    
    def pop_back(self):
        if self.size() == 0:
            return -1
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size() == 0:
            return -1
        return self.queue[0]
    
    def back(self):
        if self.size() == 0:
            return -1
        return self.queue[-1]

if __name__ == '__main__':
    n = int(input())
    s = MyDeque()
    for i in range(n):
        command = []
        command = input().split()
        if command[0] == 'push_front':
            s.push_front(command[1])
        elif command[0] == 'push_back':
            s.push_back(command[1])
        elif command[0] == 'pop_front':
            print(s.pop_front())
        elif command[0] == 'pop_back':
            print(s.pop_back())
        elif command[0] == 'size':
            print(s.size())
        elif command[0] == 'empty':
            print(s.empty())
        elif command[0] == 'front':
            print(s.front())
        elif command[0] == 'back':
            print(s.back())