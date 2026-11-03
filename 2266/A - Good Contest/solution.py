import sys 
 
def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    t = int(input_data[0])
    i= 1
    
    for _ in range(t):
        n = int(input_data[i])
        a = int(input_data[i+1])
        b = int(input_data[i+2])
        c = int(input_data[i+3])
        i += 4
        
        ans= n - min(a,b,c)
        print(ans)
        
if __name__ == '__main__':
    solve()