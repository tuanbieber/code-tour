from collections import defaultdict
from collections import OrderedDict

class Solution:
    def __init__(self):
        pass

    def sort(self, str):
        m = defaultdict(int)
        for ele in str:
            m[ele] += 1
        
        a = sorted(m.items(), key = lambda item: item[1], reverse=True)
        
        res = "".join([word*count for word, count in a])
        print(res)

def main():
    solution1 = Solution()
    str = 'nguyenthanhtuan'
    solution1.sort(str)
    print(['a']*3)
    print(['a' * 3])

if __name__ == '__main__':
    main()

# https://leetcode.com/problems/sort-characters-by-frequency/discuss/697449/Python-1-Liner-(Beats-99.21)
