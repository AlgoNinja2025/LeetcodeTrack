# Last updated: 7/21/2026, 7:10:15 PM
class Solution(object):
  def combinationSum(self, candidates, target):
    res = []  # To store the final result
    self.backtrack(candidates, 0, target, [], res)
    return res

  def backtrack(self, candidates, start, target, comb, res):
    # If target is 0, we have found a valid combination
    if target == 0:
      # Append a copy of the current combination to the result list
      res.append(list(comb))
      return
    # Iterate through the candidates array starting from the given index
    for i in range(start, len(candidates)):
      # If the current candidate is greater than the remaining target, move on to the next
      if target < candidates[i]:
        continue
      # Add the current candidate to the current combination
      comb.append(candidates[i])
      # Recursively call the function with the updated combination and remaining target
      self.backtrack(candidates, i, target - candidates[i], comb, res)
      # Backtrack by removing the last added candidate from the combination
      comb.pop()