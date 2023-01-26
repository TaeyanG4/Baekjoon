k, n = map(int, input().split())
lines = sorted([int(input()) for _ in range(k)])

def binary_search(lines, n, start, end):
    while start <= end:
        mid = (start + end) // 2
        count = 0
        for line in lines:
            count += line // mid
        if count >= n:
            start = mid + 1
        else:
            end = mid - 1
    return end

print(binary_search(lines, n, 1, lines[-1]))