FILE_SIZE = 1860000

def main():
    cnt = 0
    while True:
        cnt += 1
        try:
            sz = int(input())
        except ValueError:  # Handle non-integer inputs gracefully
            print("Please enter a valid integer.")
            continue
        if not sz:
            break
        if sz % 2:
            sz = sz // 2 + 1
        else:
            sz //= 2
        sz += sz // 2
        print(f"File #{cnt}")
        print(f"John needs {(sz + FILE_SIZE - 1) // FILE_SIZE} floppies.\n")

if __name__ == "__main__":
    main()