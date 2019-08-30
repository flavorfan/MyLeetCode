#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
from typing import List
import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words=sorted(words)
        tem=collections.Counter(words).most_common(k)
        # print(tem)
        return [i[0] for i in tem]

    def topKFrequent_lazy(self, words: List[str], k: int) -> List[str]:
        import collections
        from functools import cmp_to_key
        counts = collections.Counter(words)
        def _cmp(x, y):
            if counts[x] == counts[y]:
                if x < y:
                    return -1
                else:
                    return 1
            else:
                if counts[x] < counts[y]:
                    return 1
                elif counts[x] > counts[y]:
                    return -1
        # python3 not work  return sorted(counts.keys(), cmp=_cmp)[:k]
        return sorted(counts.keys(), key = cmp_to_key(_cmp))[:k]
if __name__ == '__main__':
    sln = Solution()
    print( sln.topKFrequent_lazy(["i", "love", "leetcode", "i", "love", "coding"], 2))

