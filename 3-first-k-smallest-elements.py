import random

class Solution:
    def __init__(self):
        pass

    def firstK_one(self, lst, K):
        lst.sort(key = lambda x: x)
        return lst[:K]

    def firstK_two(self, lst, K):
        low = 0
        high = len(lst) - 1
        self.quickSelect(lst, low, high, K)
        return lst[:K]
    
    def quickSelect(self, lst, low, high, K):
        if len(lst) < K or K == 0: return []
        if low < high:
            pivot = self.partition(lst, low, high)
            if K <= pivot + 1:
                self.quickSelect(lst, low, pivot - 1, K)
            else:
                self.quickSelect(lst, pivot + 1, high, K )

    def partition(self, lst, low, high):
        # move the pivot to the right position
        pivot = lst[high]
        buffer = low
        for idx in range(low, high):
            if lst[idx] < pivot:
                lst[idx], lst[buffer] = lst[buffer], lst[idx]
                buffer += 1

        lst[buffer], lst[high] = lst[high], lst[buffer]
        
        return buffer # cost O(n) time complexity

s1 = Solution()
lst = [1,4,6,7,-84,0,3764,76,100,32]
k = 4
print(lst)
res = s1.firstK_two(lst, k)
print('------------------')
print(res)

# https://leetcode.com/articles/k-closest-points-to-origin/