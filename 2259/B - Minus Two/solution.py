import sys
 
def main():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    results = []
    
    for _ in range(t):
    
        n = int(input_data[idx])
        idx += 1
        
        
        vec = [int(input_data[idx + i]) for i in range(n)]
        idx += n
        
        mod_4 = [0, 0, 0, 0]
        for x in vec:
            mod_4[x % 4] += 1
            
        ans = max(mod_4[0], mod_4[2], mod_4[1] + mod_4[3])
        results.append(str(ans))
        
    print('
'.join(results))
 
if __name__ == '__main__':
    main()