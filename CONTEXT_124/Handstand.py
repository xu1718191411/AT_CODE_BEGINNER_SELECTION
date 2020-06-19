N, K = map(int, input().split())
S = input()


def calculate(n, k, s):
    s = list(s)

    result = [{'start': 0, 'end': 0}]
    for i in range(n):

        previous = s[i - 1]
        current = s[i]

        if i == 0:
            if s[i] == '1':
                result.append({'start': 0})
        else:
            if (current == '0') and (previous == '1'):
                res = result[-1]
                res.__setitem__('end', i)
                result[-1] = res

            if (current == '1') and (previous == '0'):
                result.append({'start': i})

        if i == n - 1 and s[i] == '1':
            res = result[-1]
            res.__setitem__('end', i + 1)
            result[-1] = res

    result.append({'start': n, 'end': n})

    # print(result)
    maxValue = 0
    if len(result) > k:
        for i in range(len(result) - k):
            val = result[i + k]['end'] - result[i]['start']
            maxValue = max(val, maxValue)
    else:
        maxValue = max(maxValue, result[-1]['end'] - result[0]['start'])

    print(maxValue)


calculate(N, K, S)
