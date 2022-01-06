def encode(arr):
    # Code here
    n = len(arr)
    prev = arr[0]
    res = ''
    count = 1
    for i in range(1,n):
        if prev == arr[i]:
            count += 1
        else: 
            res = res + prev + str(count)
            prev = arr[i]
            count = 1
    res = res + prev + str(count)
    return res