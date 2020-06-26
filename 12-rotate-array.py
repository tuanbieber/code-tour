class Solution:
    def __init__(self):
        pass

    def rotate(self, k, nums):
        nums = nums[len(nums) - k:] + nums[:len(nums)-k]
        print('this is in function ', id(nums))
        nums = 0

def main():
    solution1 = Solution()
    nums = [-1,-100,3,99]
    print('this is in main ', id(nums))
    k = 2
    solution1.rotate(k, nums)
    print('this is nums ', nums)

if __name__ == '__main__':
    main()

# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/
