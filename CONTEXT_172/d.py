N = int(input())

def calculate(n):
    result = 0
    for i in range(1, n + 1):
        num = n // i
        if num == 1:
            result += i
        else:
            start = i
            end = num * i
            total = ((start + end) * num) // 2
            result += total

    print(result)


calculate(N)
