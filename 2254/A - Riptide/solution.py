import sys
 
 
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
 
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        v = [int(data[idx]), int(data[idx + 1]), int(data[idx + 2])]
        idx += 3
        v.sort()
        out.append(str(min(v[2] - v[1], v[1] - v[0])))
 
    print("
".join(out))
 
 
if __name__ == "__main__":
    main()