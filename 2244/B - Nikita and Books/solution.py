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
        idx += 1
        a = list(map(int, input_data[idx : idx + n]))
        idx += n
 
        prefix_sum = 0
        possible = True
 
        for k in range(1, n + 1):
            prefix_sum += a[k - 1]
            required = k * (k + 1) // 2
            if prefix_sum < required:
                possible = False
                break
 
        out.append("YES" if possible else "NO")
 
    print("
".join(out))
 
 
if __name__ == "__main__":
    solve()