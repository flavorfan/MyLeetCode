#
# @lc app=leetcode id=1036 lang=python3
#
# [1036] Escape a Large Maze
#

# @lc code=start
from typing import List
class Solution:
    # 164ms 93.23%
    # 阶梯的关键是　is_in_box 判断是否有概率在ｂｌｏｃｋｅｄ围成ｂｏｘ中，让探索可以有界限
    # 由于ｓｒｃ或者ｔａｒｇｅｔ都有可能被ｂｌｏｃｋ住，所以需要从两个方向进行探索
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set([(x[0], x[1]) for x in blocked])

        def gen_neighbor(x, y):
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if x + dx < 0 or x + dx > 1e6 or y + dy < 0 or y + dy > 1e6:
                    continue
                nx, ny = x + dx, y + dy
                yield nx, ny

        # 离开足够远，block中的障碍不足以围住
        def is_in_box(x, y, center_x, center_y, length):
            return center_x - length <= x <= center_x + length and \
                center_y - length <= y <= center_y + length


        def is_blocked(start_x, start_y, end_x, end_y):
            seen = set()
            stack = [(start_x, start_y)]
            seen.add((start_x, start_y))
            while stack:
                x, y = stack.pop(-1)
                if not is_in_box(x, y, start_x, start_y, len(blocked)) or \
                        (x == end_x and y == end_y):
                    return True

                for nx, ny in gen_neighbor(x, y):
                    if (nx, ny) in blocked or (nx, ny) in seen: continue
                    seen.add((nx, ny))
                    stack.append((nx, ny))
            return False

        return is_blocked(source[0], source[1], target[0], target[1]) and \
               is_blocked(target[0], target[1], source[0], source[1])
# @lc code=end

if __name__ == '__main__':
    sln =Solution()
    blocked = [[0,1],[1,0]] 
    source = [0,0]
    target = [0,2]
    print(sln.isEscapePossible(blocked,source,target))


