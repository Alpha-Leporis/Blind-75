# Word Break

# https://leetcode.com/problems/word-break/description/

'''

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.

'''

# solution: DP bottom-up

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # [False, False, False, False, False, False, False, False, False]
        dp[len(s)] = True # [False, False, False, False, False, False, False, False, True]
        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                # print(w, i, len(w), s[i: i + len(w)], s[i: i + len(w)] == w)
                    # ('leet', 7, 4, 'e', False)
                    # ('code', 7, 4, 'e', False)
                if(i + len(w)) <= len(s)and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)] # or dp[i] = True     --> dp[4] = dp[4 + 4] , dp[0] = dp[0 + 4]

                if dp[i]: # if dp[i] is True then we break --> dp[4] is true --> dp[0] is true
                    break
        return dp[0]
    
# dp = [True, False, False, False, True, False, False, False, True]

# TC: O(n * m)
# SC: O(n * m)


'''
explaination:

# print(w,  i, len(w), s[i: i + len(w)], s[i: i + len(w)] == w)        ('leet', 7, 4, 'e', False)
                                                                      ('code', 7, 4, 'e', False)

i=7      leet 7 4 11 8 e False
         code 7 4 11 8 e False
i=6      leet 6 4 10 8 de False
         code 6 4 10 8 de False
i=5      leet 5 4 9 8 ode False
         code 5 4 9 8 ode False
i=4      leet 4 4 8 8 code False
         code 4 4 8 8 code True
i=3      leet 3 4 7 8 tcod False
         code 3 4 7 8 tcod False
i=2      leet 2 4 6 8 etco False
         code 2 4 6 8 etco False
i=1      leet 1 4 5 8 eetc False
         code 1 4 5 8 eetc False
i=0      leet 0 4 4 8 leet True


# if(i + len(w)) <= len(s) and s[i: i + len(w)] == w:
    dp[i] = dp[i + len(w)] # dp[4] = dp[8], dp[0] = dp[4]  --> dp[0] = dp[4] = dp[8]
    
7 + 4 <= 8 and [7: 7 + 4] == 11 <= 8 and 'leet' --> 'e' == 'code' --> False
7 + 4 <= 8 and [7: 7 + 4] == 11 <= 8 and 'code' --> 'e' == 'code' --> False

6 + 4 <= 8 and [6: 6 + 4] == 10 <= 8 and 'leet' --> 'de' == 'leet' --> False
6 + 4 <= 8 and [6: 6 + 4] == 10 <= 8 and 'code' --> 'ode' == 'code' --> False

5 + 4 <= 8 and [5: 5 + 4] == 9 <= 8 and 'leet' --> 'ode' == 'leet' --> False
5 + 4 <= 8 and [5: 5 + 4] == 9 <= 8 and'code' --> 'ode' == 'code' --> False

4 + 4 <= 8 and [4: 4 + 4] == 8 <= 8 and 'leet' --> code == 'leet' --> False
4 + 4 <= 8 and [4: 4 + 4] == 8 <= 8 and 'code' --> 'code' == 'code' --> True

3 + 4 <= 8 and [3: 3 + 4] == 'leet' --> 'tcod' == 'leet' --> False
3 + 4 <= 8 and [3: 3 + 4] == 'code' --> 'tcod' == 'code' --> False

2 + 4 <= 8 and [2: 2 + 4] == 'leet' --> 'etco' == 'leet' --> False 
2 + 4 <= 8 and [2: 2 + 4] == 'code' --> 'etco' == 'code' --> False

1 + 4 <= 8 and [1: 1 + 4] == 'leet' --> 'eetc' == 'leet' --> False 
1 + 4 <= 8 and [1: 1 + 4] == 'code' --> 'eetc' == 'code' --> False

0 + 4 <= 8 and [0: 0 + 4] == 'leet' --> 'leet' == 'leet' --> True 
0 + 4 <= 8 and [0: 0 + 4] == 'code' --> 'leet' == 'code' --> False

output:

i  =    0    1      2      3      4     5      6      7      8
dp = [True, False, False, False, True, False, False, False, True]


'''