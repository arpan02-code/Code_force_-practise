import sys
 
 
def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
 
  t = int(input_data[0])
  out = []
  idx = 1
 
  for _ in range(t):
    a = int(input_data[idx])
    b = int(input_data[idx + 1])
    c = int(input_data[idx + 2])
    idx += 3
 
    # Sort the numbers such that nums[0] <= nums[1] <= nums[2]
    nums = sorted([a, b, c])
 
    # The minimum possible range is the minimum between the initial range (nums[2] - nums[0]) 
    # and the median value (nums[1]).
    ans = min(nums[2] - nums[0], nums[1])
    out.append(str(ans))
 
  print("
".join(out))
 
 
if __name__ == "__main__":
  solve()