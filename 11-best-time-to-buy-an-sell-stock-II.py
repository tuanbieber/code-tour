class Solution:
    def __init__(self):
        pass

    def maxProfit(self, nums):
        max = 0
        for i in range(0, len(prices)-1):
            if (prices[i+1] > prices[i]):
                max += prices[i+1] - prices[i]
        return max

def main():
    solution1 = Solution()
    nums = [7,1,5,3,6,4]

    res = solution1.maxProfit(nums)
    print('this is res ', res)

if __name__ == '__main__':
    main()

# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/
