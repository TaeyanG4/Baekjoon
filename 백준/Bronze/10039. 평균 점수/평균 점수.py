if __name__ == '__main__':
    var = []
    result = 0
    for i in range(0, 5):
        var.append(int(input()))
        if var[i] < 40:
            var[i] = 40
        result += var[i]

    print(int(result/5))
