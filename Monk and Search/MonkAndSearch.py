def search(arr, key):
    si = 0
    li = len(arr) - 1
    while si < li:
        mid = (si + li) // 2
        if arr[mid] >= key:
            li = mid
        else:
            si = mid + 1
    return li

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
q = int(input())
for _ in range(q):
    o,x = map(int, input().split())
    x += o
    if x > arr[len(arr)-1]:
        print("0")
    elif x < arr[0]:
        print(len(arr))
    else:
        index = search(arr, x)
        print( n - index)