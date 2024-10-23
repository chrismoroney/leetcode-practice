from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  discs_to_deflate = 0
  max_disc_size = R[N-1]
  for i in range(N-2, -1, -1):
    print(R[i])
    if max_disc_size == 0:
      return -1
    
    if R[i] >= max_disc_size:
      discs_to_deflate += 1
      max_disc_size -= 1
    else:
      max_disc_size = R[i]
  return discs_to_deflate

if __name__ == "__main__":
  N = 5
  R = [2, 5, 3, 6, 5]
  print("answer: ", getMinimumDeflatedDiscCount(N, R))