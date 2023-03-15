def check_lineup(beards):
    sorted_beards = sorted(beards)
    if beards == sorted_beards or beards == sorted_beards[::-1]:
        return "Ordered"
    return "Unordered"

def main():
    n = int(input())
    print("Gnomes:")
    for _ in range(n):
        beards = list(map(int, input().split()))
        result = check_lineup(beards)
        print(result)

if __name__ == "__main__":
    main()