import sys
 
def solve():
    raw_data = sys.stdin.read().split()
    if not raw_data:
        return
    
    it = iter(raw_data)
    num_tests = int(next(it))
    ans = []
    
    for _ in range(num_tests):
        length = int(next(it))
        arr = [int(next(it)) for _ in range(length)]
        
        curr = 0
        for val in reversed(arr):
            curr = 2 * val - curr
            
        p = curr // 2
        ans.append(str(p))
        
    print('
'.join(ans))
 
if __name__ == '__main__':
    solve()