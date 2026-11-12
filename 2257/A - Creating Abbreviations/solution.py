import sys
 
def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        available_chars = set()
        for _ in range(n):
            word = data[idx]
            idx += 1
            available_chars.add(word[0].lower())
            
        possible = True
        for _ in range(m):
            abbr = data[idx]
            idx += 1
            # Check every character in the abbreviation
            for char in abbr:
                if char.lower() not in available_chars:
                    possible = False
                    
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('
'.join(out))
 
if __name__ == '__main__':
    solve()