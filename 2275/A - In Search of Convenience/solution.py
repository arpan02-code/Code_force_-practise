import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    out = []
    idx = 1
    for _ in range(t):
        x0 = int(input_data[idx])
        y0 = int(input_data[idx+1])
        R = int(input_data[idx+2])
        idx += 3
        out.append(f"{x0} {y0 + R}")
    print("
".join(out))
 
if __name__ == '__main__':
    solve()