N = int(input())
ARR = [int(s) for s in input().split(" ")]
def calculate(arr,n):
    return sum(arr) - n

result = calculate(ARR,N)
print(result)