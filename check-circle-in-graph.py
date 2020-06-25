import collections

class Solution():
    def __init__(self):
        pass
    def circle(self, n, lst):
        adjacent = collections.defaultdict(list)

        for u, v in lst:
            adjacent[u].append(v)
            adjacent[v].append(u)

        color = ['none'] * n

        color[0] = 'red'

        for vertex in range(1, n + 1):
            if color[vertex] == 'none':
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                


        return False

solution1 = Solution()
lst = [[1,2],[2,3],[3,4],[4,5],[1,5], [4, 1], [6,7]]
n = 7
res  = solution1.circle(n, lst)
print(res)