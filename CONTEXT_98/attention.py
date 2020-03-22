N = int(input())
S = input()


def calculate(S):
    SSS = []

    totalENum = S.count("E")

    for index, value in enumerate(S):
        if index == 0:
            obj = {}
            if value == "W":
                obj.__setitem__("W", 1)
                obj.__setitem__("E", 0)
            else:
                obj.__setitem__("E", 1)
                obj.__setitem__("W", 0)
            SSS.append(obj)
        else:
            obj = {}
            prevW = SSS[index - 1].__getitem__("W")
            prevE = SSS[index - 1].__getitem__("E")
            if value == "W":
                obj.__setitem__("W", prevW + 1)
                obj.__setitem__("E", prevE)
            else:
                obj.__setitem__("E", prevE + 1)
                obj.__setitem__("W", prevW)

            SSS.append(obj)

    resVal = len(S)
    for index,value in enumerate(S):
        if value == "W":
            resVal = min(resVal,SSS[index].__getitem__("W") - 1 + totalENum - SSS[index].__getitem__("E"))
        else:
            resVal = min(resVal, SSS[index].__getitem__("W") + totalENum - SSS[index].__getitem__("E"))

    return resVal


result = calculate(S)

print(result)
