import sys
 
def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return 
    
    t = int(input_data[0])
    i =1 
    out =[]
    
    for _ in range(t):
        a = int(input_data[i])
        b = int(input_data[i+1])
        
        i += 2
        if a <=b :
            out.append("-1")
            
        else:
            out.append(str(min(b,a-b)))
    print('
'.join(out))
 
if __name__ == "__main__":
  solve()