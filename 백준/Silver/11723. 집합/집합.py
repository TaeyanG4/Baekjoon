import sys

class MySet:
    def __init__(self):
        self.arr = [0] * 20
        
    def add(self, x):
        self.arr[x-1] = 1
    
    def remove(self, x):
        self.arr[x-1] = 0
    
    def check(self, x):
        return self.arr[x-1]
    
    def toggle(self, x):
        self.arr[x-1] = 1 - self.arr[x-1]
        
    def all(self):
        self.arr = [1] * 20
    
    def empty(self):
        self.arr = [0] * 20

if __name__ == '__main__':
    input = sys.stdin.readline
    
    n = int(input())
    S = MySet()
    for i in range(n):
        user_input = input().strip().split()
        if len(user_input) == 2:
            command, value = user_input
            if command == 'add':
                S.add(int(value))
            elif command == 'remove':
                S.remove(int(value))
            elif command == 'check':
                print(S.check(int(value)))
            elif command == 'toggle':
                S.toggle(int(value))
        else:
            command = user_input[0]
            if command == 'all':
                S.all()
            elif command == 'empty':
                S.empty()