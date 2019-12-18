#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start

# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

from typing import List
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # Build a library that connects employee id and list index
        lib = {}
        for i in range(len(employees)):
            lib[employees[i].id] = i
        
        # Prepare a stack of id and result value
        stack = [id]
        res = 0
        
        # Keep doing it until the stack gets empty
        while stack:
            one_employee = stack.pop() # Take one employee from the stack
            res += employees[lib[one_employee]].importance # Update the result value
            for i in employees[lib[one_employee]].subordinates: # Add all subordinates of this employee to the stack
                stack.append(i)
        
        return res
# @lc code=end

if __name__ == '__main__':
    sln = Solution()
    em = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    print(sln.getImportance(em,id))
