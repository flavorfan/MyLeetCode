#
# @lc app=leetcode id=753 lang=python3
#
# [753] Cracking the Safe
#

# @lc code=start
# Hierholzer 算法可以在一个欧拉图中找出欧拉回路
# 我们从任意节点 u 开始，任意地经过未经过的边，直到我们“无路可走”。
# 可以发现，我们最终一定会停在节点 u，这是因为所有节点的入度和出度都相等。

# 我们得到了一条从 u 开始到 u 结束的回路，这条回路上仍然有些节点有未经过的出边。
# 我么从某个这样的节点 v 开始，把 v 看成 u，继续得到一条从 v 开始到 v 结束的回路，
# 再嵌入之前的回路中，即 u -> ... -> v -> ... -> u 变为 u -> ... -> v -> ... -> v -> ... -> u。
# 以此类推，直到没有未经过的边，此时我们就找到了一条欧拉回路。

# 48ms 77.31%
# python由于是值传递，可以通过给函数传list的方式，直接修改list内会导致外边的List也变化，
# 但是传string不行。string是不可变的对象，函数内部修改string不会影响到外边。
class Solution_1:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        ans = []
        def dfs(node):
            for x in map(str, range(k)):  # 获得　"0" "1" "2" ... "k"
                nei = node + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei[1:])
                    ans.append(x)

        dfs("0" * (n-1))
        return "".join(ans) + "0" * (n-1)

# Inverse Burrows-Wheeler Transform
# 38ms 98.21
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        M = k**(n-1)
        # ｋ进制进位
        P = [q*k+i for i in range(k) for q in range(M)]
        ans = []

        for i in range(k**n):
            j = i
            while P[j] >= 0:
                ans.append(str(j // M))
                P[j], j = -1, P[j]

        return "".join(ans) + "0" * (n-1)
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    print(sln.crackSafe(4,2))

