def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True

def solution(n, k):
    answer = 0
    num_str = ""

    while n > 0:
        num_str = str(n%k) + num_str
        n = n//k


    arr = num_str.split('0')
    for i in arr:
        if i != '':
            if isitPrime(int(i)):
                answer+=1

    return answer