import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    out = []
    idx = 1
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        idx += 2
        
        if b > a + 1:
            out.append("-1")
        elif a % 2 == b % 2:
            out.append(str(a))
        else:
            out.append(str(a + 1))
            
    print('
'.join(out))
 
solve()