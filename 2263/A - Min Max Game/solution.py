import sys
 
 
def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
 
    t = int(data[0])
    idx = 1
 
    for _ in range(t):
        n = int(data[idx])
        idx += 1
 
    
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
 
        
        cnt = sum(a)
 
        if cnt >= n - cnt:
            print("Bessie")
        else:
            print("Elsie")
 
 
if __name__ == "__main__":
    solve()