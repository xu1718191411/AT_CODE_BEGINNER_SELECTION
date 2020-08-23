S = input()

arr = S.split("S")


brr = [len(arr[i]) for i in range(len(arr))]


print(max(brr))
