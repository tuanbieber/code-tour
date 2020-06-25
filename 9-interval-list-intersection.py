from collections import defaultdict
from collections import OrderedDict

class Solution:
    def __init__(self):
        pass

    def sort(self, A, B):
        res = []
        i = j = 0

        while i < len(A) and j < len(B):
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])
            if low <= high:
                res.append([low, high])
            if A[i][1] < B[j][1]:
                i += 1
            else: 
                j += 1
        print(res)
        return 0

def main():
    solution1 = Solution()
    A = [[0,2],[5,10],[13,23],[24,25]]
    B  = [[1,5],[8,12],[15,24],[25,26]]
    solution1.sort(A, B)


if __name__ == '__main__':
    main()

# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/
