import itertools

def calculate(n):
    arr = ["a", "b", "c"]

    for item in itertools.product(arr,repeat=n):
        print("".join(list(item)))


calculate(int(input()))
