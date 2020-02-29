n = int(input())
arr = [int(s) for s in input().split(" ")]

def calculate(n,arr):
    arr = sorted(arr)
    data = []
    for i in range(1,101):
        sum = 0
        for ar in arr:
            sum += (ar - i) ** 2

        data.append(sum)

    return min(data)


result = calculate(n,arr)

print(result)