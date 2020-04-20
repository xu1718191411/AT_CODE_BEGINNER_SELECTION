N = int(input())
ARR = list(map(int,input().split()))

def calculate(n,arr):

    result = [set() for i in range(n)]

    for index,ar in enumerate(arr):
        ar = ar - 1
        result[ar].add(index+1)


    for res in result:
        print(len(res))

calculate(N,ARR)