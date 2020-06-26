# solution 1:

def singleNumber(lst):
    return 2 * sum(set(lst)) - sum(lst)

lst = [1,1,5,6,7,8,9,8,6,5,7]
res = singleNumber(lst)
print(res)

# solution 2: bit manipulation

def solution2(lst):
    res = 0
    for item in lst:
        res ^= item
    return res

res2 = solution2(lst)
print('bit manipulation ', res2)

# solution 3: hash map 



