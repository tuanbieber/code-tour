class Solution:
    def __init__(self):
        pass

    def function1(self, nums):
        if len(nums) == 0: 
            return 0
        if len(nums) == 1: 
            return 1
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j] 
        return i + 1

def main():
    solution1 = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    res = solution1.function1(nums)
    print('this is res ', res)


if __name__ == '__main__':
    main()

# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/
