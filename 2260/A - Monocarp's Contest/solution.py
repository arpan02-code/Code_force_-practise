t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    zeros = a.count(0)
 
    if zeros < 2:
        print(-1)
    else:
        ans = 0
 
        if a[0] == 1:
            ans += 1
 
        if a[n - 1] == 1:
            ans += 1
 
        print(ans)