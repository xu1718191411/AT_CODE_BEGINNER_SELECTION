N = int(input())

def calculate2(n):
    arr = []
    for i in range(40):

        if n % (2**(i+1)) != 0:
            arr.append(1)
            n = n - ((-2) ** i)
        else:
            arr.append(0)
        if n == 0:
            break

    arr.reverse()
    return arr

result = calculate2(N)
result = "".join([str(s) for s in result])
print(result)