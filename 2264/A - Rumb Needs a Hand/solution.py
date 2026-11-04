import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        p = []
        for i in range(n):
            p.append(int(input_data[idx]))
            idx += 1
            
        # Find indices where elements are not at their correct position (1-based value compared to index+1)
        bad = []
        for i in range(n):
            if p[i] != i + 1:
                bad.append(i)
                
        ok = True
        k = len(bad)
        # Check if the mismatched elements form a mirror-symmetric pattern
        for i in range(k):
            if p[bad[i]] != bad[k - 1 - i] + 1:
                ok = False
                break
                
        if ok:
            print("YES")
        else:
            print("NO")
 
if __name__ == '__main__':
    solve()