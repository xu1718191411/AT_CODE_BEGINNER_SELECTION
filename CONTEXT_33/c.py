S = "3*1*4+0+2*0+5*2+9*8*6+1+3"
S = input()
def calculate(s):
    arr = s.split("+")
    # print(arr)

    result = 0
    for i in range(len(arr)):
        if not arr[i].__contains__("0"):
            result += 1

    print(result)
calculate(S)