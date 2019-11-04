def coins():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    AVALUE = 500
    BVALUE = 100
    CVALUE = 50

    XA = 0
    XB = 0
    XC = 0

    XAMAX = A if A*AVALUE <= X else int(X/AVALUE)
    XBMAX = B if C*BVALUE <= X else int(X/BVALUE)
    XCMAX = C if C*CVALUE <= X else int(X/CVALUE)

    parametersCombineList = calculatePossibility([XAMAX,XBMAX,XCMAX])



def calculatePossibility(arr):
    totalPossibilities = 0
    for i in arr:
        print(i)
        if i == 0:
            continue
        if totalPossibilities == 0:
            totalPossibilities = 1
        totalPossibilities *= i


    result = []

    for i in range(totalPossibilities):
        result.append([])
    print("totalPossibilities")
    print(totalPossibilities)




coins()

