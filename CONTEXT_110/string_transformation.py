S = input()
T = input()

def calculate(s, t):
    dictS = {}
    dictT = {}

    for ss in s:
        if dictS.get(ss) == None:
            dictS.__setitem__(ss, 1)
        else:
            dictS.__setitem__(ss, dictS.get(ss) + 1)

    for tt in t:
        if dictT.get(tt) == None:
            dictT.__setitem__(tt, 1)
        else:
            dictT.__setitem__(tt, dictT.get(tt) + 1)

    sValues = dictS.values()
    tValues = dictT.values()

    sNums = {}
    tNums = {}


    for value in sValues:
        if sNums.get(value) == None:
            sNums.__setitem__(value,1)
        else:
            sNums.__setitem__(value,sNums.get(value) + 1)

    for value in tValues:
        if tNums.get(value) == None:
            tNums.__setitem__(value,1)
        else:
            tNums.__setitem__(value,tNums.get(value) + 1)

    if (sNums == tNums):
        print("Yes")
    else:
        print("No")

calculate(S, T)
