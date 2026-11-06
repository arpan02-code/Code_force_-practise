import sys
 
def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    T = int(data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        c = s.count('1')
        if c <= 2:
            out.append(str(c - 1))
            continue
            
        l = s.find('1')
        r = s.rfind('1')
        out.append(str(r - l))
        
    print('
'.join(out))
 
if __name__ == '__main__':
    solve()