from collections import defaultdict
import collections
class Solution:
    def __init__(self):
        pass

    def bipartition(self,n, dislikes):
        adjacent = defaultdict(list)
        for u, v in dislikes:
            adjacent[u].append(v)
            adjacent[v].append(u)

        queue = []
        color = [0] * n

        for vertex in range(1, n+1):
            if len(adjacent[vertex]) == 1:
                queue.append(vertex)

        while queue:
            current = queue.pop(0)



solution1 = Solution()
n = 5
dislikes = [[1,2],[3,4],[4,5],[3,5]]
res = solution1.bipartition(n, dislikes)
print(res)

# https://leetcode.com/problems/possible-bipartition/solution/