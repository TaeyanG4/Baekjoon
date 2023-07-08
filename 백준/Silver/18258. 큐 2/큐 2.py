# import lines
#################################
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from itertools import *
# from heapq import *
# from datetime import datetime
# from bisect import *
#################################

class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        else:
            return -1

# def solution(n):
#     pass

if __name__ == '__main__':
    input = sys.stdin.readline
    # sys.setrecursionlimit(10**6)
    
    # input
    n = int(input().rstrip())

    # output
    queue = Queue()
    for _ in range(n):
        command = input().rstrip()
        if command == 'pop':
            print(queue.pop())
        elif command == 'size':
            print(queue.size())
        elif command == 'empty':
            print(queue.empty())
        elif command == 'front':
            print(queue.front())
        elif command == 'back':
            print(queue.back())
        else:
            command, x = command.split()
            queue.push(x)
