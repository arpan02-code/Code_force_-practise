import sys
 
def solve():
    # Fast input ke liye
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        a = [0] * (n + 1)
        cnt = [0] * 101
        
        for i in range(1, n + 1):
            a[i] = int(input_data[idx])
            idx += 1
            cnt[a[i]] += 1
            
        current_ans = []
        for i in range(1, n + 1):
            for j in range(100, 0, -1):
                if cnt[j] >= i:
                    current_ans.append(str(j))
                    
        out.append(" ".join(current_ans))
        
    print("
".join(out))
 
if __name__ == '__main__':
    solve()