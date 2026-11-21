import sys
 
 
def solve():
  data = sys.stdin.read().split()
  if not data:
    return
 
  t = int(data[0])
  idx = 1
  out = []
 
  for _ in range(t):
    n = int(data[idx])
    idx += 1
    a = list(map(int, data[idx : idx + n]))
    idx += n
 
    if sum(a) % 4 == 0:
      out.append("YES")
    else:
      out.append("NO")
 
  print("
".join(out))
 
 
if __name__ == "__main__":
  solve()