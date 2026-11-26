t = int(input())
 
for _ in range(t):
  n = int(input())
  s = input().strip()
 
  max_len = 0
  curr_len = 0
 
  for ch in s:
    if ch == "#":
      curr_len += 1
      if curr_len > max_len:
        max_len = curr_len
    else:
      curr_len = 0
 
  if max_len == 0:
    print(0)
  else:
    print((max_len + 1) // 2)