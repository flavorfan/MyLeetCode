#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
# 1 选点
# 我们把每个邮箱地址当成点，为什么这么选取呢？
# （因为emai具有唯一性，而name没有）
# 2 取边
# 对于accounts中的一个List
# ["name","emal1","emai2","email3"]
# 我们只需让eami1与eaml2相连，email2与eamls3相连，则三个email就两两相连，处于同一个连通块中

# 把额外信息存放到  em_to_id em_to_name dict

from typing import List
import collections
class UnionFind:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size =[1] * n

    def find(self,p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p
    def union(self, p, q):
        idp, idq = self.find(p), self.find(q)
        if idp == idq:
            return False
        
        less, more = ((idp, idq) if self.size[idp] < self.size[idq] else (idq, idp))

        self.id[less] = self.id[more] 
        self.size[more] += self.size[less]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(10001)

        em_to_name ={}
        em_to_id={}
        i = 0 
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:   
                em_to_name[email] = name
                if email not in em_to_id: 
                    em_to_id[email] = i 
                    i += 1 
                uf.union(em_to_id[acc[1]], em_to_id[email]) 
        
        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[uf.find(em_to_id[email])].append(email)
        
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]    




if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
     ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"],["Mary", "mary@mail.com"]]
    sln = Solution()
    print(sln.accountsMerge(accounts))