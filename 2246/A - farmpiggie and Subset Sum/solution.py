t = int(input())
 
for _ in range(t):
    n = int(input())
    ans = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            ans.append(i + 1)
        else:
            ans.append(i - 1)
    print(*ans)