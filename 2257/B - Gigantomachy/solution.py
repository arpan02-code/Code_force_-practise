t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    x = a[0] + n - 1
    y = b[0] + m - 1
 
    if x >= y:
        print(1)
    else:
        print(2)