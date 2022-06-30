n,x = map(int, input().split())
a = list(map(int, input().split()))
arr = [0]
chk = 0
for i in range(n):
    arr.append(arr[i]+a[i])
    if a[i] > x:
        chk = 1
if chk == 1:
    print("-1")
elif arr[n] < x:
    print(n)
else:
    si = 1
    li = n
    while si <= li:
        mid = (si + li) // 2
        chk = 0
        j = mid
        while j < n+1:
            if arr[j] - arr[j-mid] > x:
                break
            j += 1
        if j == n+1:
            si = mid+1
        else:
            li = mid - 1
    print(si - 1)