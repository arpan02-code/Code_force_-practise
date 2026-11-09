import sys
 
 
def main():
  data = sys.stdin.read().split()
  if not data:
    return
 
  t = int(data[0])
  idx = 1
  out = []
 
  for _ in range(t):
    n = int(data[idx])
    k = int(data[idx + 1])
    s = data[idx + 2]
    idx += 3
 
    ans = sum(1 for i in range(0, n, k) if "0" not in s[i : i + k])
    out.append(str(ans))
 
  print("
".join(out))
 
 
if __name__ == "__main__":
  main()