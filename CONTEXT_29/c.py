result = []


def calculate(n):
    materials = ["a", "b", "c"]

    for material in materials:
        dfs(n, 0, material)

    for res in result:
        print(res)

def dfs(n, currentIndex, currentValue):
    if currentIndex == (n - 1):
        result.append(currentValue)
        return

    materials = ["a", "b", "c"]
    for material in materials:
        dfs(n, currentIndex + 1, currentValue + material)

calculate(int(input()))
