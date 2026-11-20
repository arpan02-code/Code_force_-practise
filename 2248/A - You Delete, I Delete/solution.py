import sys
 
 
def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
 
  t = int(input_data[0])
  idx = 1
  out = []
 
  for _ in range(t):
    s = input_data[idx]
    idx += 1
    n = len(s)
 
    best_for_alice = None
    for i in range(n):
      if s[i] == "0":
        after_alice = s[:i] + s[i + 1 :]
        best_for_bob = None
 
        for j in range(len(after_alice)):
          if after_alice[j] == "1":
            cand = after_alice[:j] + after_alice[j + 1 :]
            if best_for_bob is None or cand < best_for_bob:
              best_for_bob = cand
 
        if best_for_alice is None or best_for_bob > best_for_alice:
          best_for_alice = best_for_bob
 
    out.append(best_for_alice)
 
  sys.stdout.write("
".join(out) + "
")
 
 
if __name__ == "__main__":
  solve()