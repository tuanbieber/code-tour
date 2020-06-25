class Solution:
    def __init__(self):
        pass

    def draft(self, word1, word2):
        width = len(word1)
        height = len(word2)
        myMatrix = [[0] * (width + 1) for i in range(height+1)]
        for r in range(1, height + 1):
            for c in range(1, width + 1):
                if word2[r-1] == word1[c-1]:
                    myMatrix[r][c] = myMatrix[r-1][c-1]
                else:
                    myMatrix[r][c] = min(  min(myMatrix[r-1][c], myMatrix[r][c-1]), myMatrix[r-1][c-1]) + 1
                    
        max_common = myMatrix[height][width]

        for row in myMatrix:
            print(row)
        print('-------------------')
        return max_common

    def lcs(self, str1, str2):
        
        return 0

solution1 = Solution()
str1 = 'horse' 
str2 = 'ros'
solution1.lcs(str1, str2)

# solution 1:
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/538/week-5-may-29th-may-31st/3346/
# time complexity O(mxn)
# space complexity O(mxn)

# solution 2:
# https://www.geeksforgeeks.org/edit-distance-dp-5/
# time complexity O(mxn)
# space comlexity O(m)