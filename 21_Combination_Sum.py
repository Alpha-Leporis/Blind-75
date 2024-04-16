# Combination Sum

# https://leetcode.com/problems/combination-sum/description/

# https://www.youtube.com/watch?v=GBKI9VSKdGg&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf&index=20


'''

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []

 

Constraints:
    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct.
    1 <= target <= 40

'''

# Solution: DFS (Backtracking)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # DFS (Backtracking)
        res = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
        
        dfs(0, [], 0)
        return res

# TC: O(2^n)
# SC: O(m * n)

'''
Explaination: Initially, we need to calculate the sum of numbers to reach our target. Perhaps a brute-force approach with recursion is necessary? That sounds like a good idea. But how do we go about it? I believe using Depth-First Search (DFS) could be the way to go.

Approach:
    1. Initialize the res variable.
    2. Define the DFS function.
    3. Within the function, initialize the i, cur, and total arguments.
    4. Check if total equals the target. If yes, we must to append into res our cur.copy
    5. Check if total exceeds the target and i exceeds the length of candidates.
    6. Append the current candidates[i] to cur.
    7. Recursively call the function with i, cur, and total + candidates[i].
    8. Remove the last number from cur (to try another one).
    9. Recursively call the function again, but increment i by 1.

'''

# Solution: DP

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for c in candidates:                                  # O(N): for each candidate
            for i in range(c, target+1):                      # O(M): for each possible value <= target
                if i == c: dp[i].append([c])
                for comb in dp[i-c]: dp[i].append(comb + [c]) # O(M) worst: for each combination
        return dp[-1]

# Time Complexity: O(M*M*N), N = len(candidates), M = target
# Space Complexity: O(M*M)
