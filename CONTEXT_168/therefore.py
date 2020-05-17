N = int(input())

def calculate(n):
    n = n % 10

    s1 = [2,4,5,7,9]
    s2 = [0,1,6,8]

    if n in s1:
        print("hon")
        return

    if n in s2:
        print("pon")
        return

    print("bon")

calculate(N)