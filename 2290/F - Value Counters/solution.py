import sys
 
input = sys.stdin.read
 
def solve():
    data = input().split()
    t = int(data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = [0] * (n + 1)
        ok = True
        
        for x in range(1, n + 1):
            b = int(data[idx])
            idx += 1
            q = b + n + 1 - x
            
            if q < 1 or q > n or p[q] != 0:
                ok = False
            else:
                p[q] = x
                
        if ok:
            out.append(" ".join(map(str, p[1:])))
        else:
            out.append("-1")
            
    print("
".join(out))
 
solve()