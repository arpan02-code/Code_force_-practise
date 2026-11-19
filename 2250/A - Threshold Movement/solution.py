import sys
 
 
def solve_case(n: int, weights: list[int]) -> str:
  # For odd 1-based positions, weight must be > k (so k < min odd weight)
  # For even 1-based positions, weight must be < k (so k > max even weight)
  low = 0
  high = 10**9 + 1
 
  for idx, w in enumerate(weights, start=1):
    if idx % 2 == 1:
      if w < high:
        high = w
    else:
      if w > low:
        low = w
 
  if n % 2 == 0 and low + 2 <= high:
    return "YES"
  return "NO"
 
 
def main() -> None:
  data = sys.stdin.read().split()
  if not data:
    return
 
  t = int(data[0])
  pos = 1
  out = []
 
  for _ in range(t):
    n = int(data[pos])
    pos += 1
    weights = list(map(int, data[pos : pos + n]))
    pos += n
    out.append(solve_case(n, weights))
 
  sys.stdout.write("
".join(out) + "
")
 
 
if __name__ == "__main__":
  main()