import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        s = input_data[idx+1]
        idx += 2
        
        stack_ = []
        used = [False] * n
        
        for i in range(n):
            if s[i] == '1':
                stack_.append(i)
            elif s[i] == '2':
                if not stack_:
                    used[i] = True
                else:
                    used[stack_[-1]] = True
                    stack_.pop()
            else:
                used[i] = True
                
        res = []
        for i in range(n):
            if not used[i]:
                res.append(i + 1)
                
        out.append(str(len(res)))
        if res:
            out.append(" ".join(map(str, res)))
        else:
            out.append("")
            
    print("
".join(out))
 
if __name__ == '__main__':
    solve()