def search(arr, key):
    si = 0
    li = len(arr) - 1
    while si < li:
        mid = (si + li) // 2
        if key >= arr[mid]:
            si = mid + 1
        else:
            li = mid
    return si

d = []
in1 = int(input())
for _ in range(in1):
    x,y = map(int, input().split())
    d.append(x*x + y*y)
d.sort()
in2 = int(input())
for _ in range(in2):
    r = int(input())
    r = r*r
    if r > d[len(d) - 1]:
        print(len(d))
    else:
        print( search(d,r))