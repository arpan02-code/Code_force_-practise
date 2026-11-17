from collections import Counter
 
 
def boss():
  n = int(input())
  arr = list(map(int, input().split()))
 
  # Find the most frequent element and its count
  maj_val, max_f = Counter(arr).most_common(1)[0]
 
  others = n - max_f
  max_majority_played = min(max_f, others + 2)
 
  total_sum = sum(arr)
  ans = (total_sum - max_f * maj_val) + max_majority_played * maj_val
  print(ans)
 
 
def main():
  for _ in range(int(input())):
    boss()
 
 
if __name__ == "__main__":
  main()