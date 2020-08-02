N = int(input())
ARR = list(map(int,input().split()))
def calculate(n, arr):
    result = []

    for i in range(n):
        result.append({'index': (i + 1), 'value': arr[i]})


    result = sorted(result, key=lambda x: -x['value'])

    for i in range(n):
        print(result[i]['index'])


calculate(N, ARR)
