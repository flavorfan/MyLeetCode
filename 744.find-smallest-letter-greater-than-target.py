#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
import bisect
from typing import List
class Solution_linearscane:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect(letters, target)
        return letters[index % len(letters)]

# @lc code=end

if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "a"
    sln =Solution()
    print(sln.nextGreatestLetter(letters,target))

