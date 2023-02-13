# import line
#################################
import sys
#################################

def sol(e, s, m):
    temp_e, temp_s, temp_m = 1, 1, 1
    for i in range(1, 7981): 
        if temp_e == 16:
            temp_e = 1
        if temp_s == 29:
            temp_s = 1
        if temp_m == 20:
            temp_m = 1
        if temp_e == e and temp_s == s and temp_m == m:
            return i
        temp_e += 1
        temp_s += 1
        temp_m += 1

if __name__ == '__main__':
    input = sys.stdin.readline
    
    # Input
    e, s, m = map(int, input().split())
    
    # Output
    print(sol(e, s, m))