import itertools
ARR = list(map(int, input().split()))

def calculate(arr):
    result = set()
    for item in itertools.combinations(arr,3):
        result.add(sum(item))
    print(sorted(list(result),key=lambda x:-x)[2])

calculate(ARR)