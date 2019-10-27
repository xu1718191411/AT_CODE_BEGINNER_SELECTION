def main():
    S = input()
    arr = ['eraser', 'erase', 'dreamer', 'dream']

    for s in arr:
        S = S.replace(s,"")

    if len(S) == 0:
        print('YES')
    else:
        print('NO')


main()
