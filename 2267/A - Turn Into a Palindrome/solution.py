import sys
 
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    T = int(data[0])
    idx = 1
    out = []
    
    for _ in range(T):
        n = int(data[idx])
        c = data[idx + 1]
        s = data[idx + 2]
        idx += 3
        
        ans = 0
        for i in range(n // 2):
            if s[i] == s[n - i - 1]:
                continue
            if s[i] == c or s[n - i - 1] == c:
                ans += 1
            else:
                ans += 2
        out.append(str(ans))
        
    print('
'.join(out))
 
if __name__ == '__main__':
    main()