# from collections import defaultdict

# def main(n, lst):
#     result = []
#     queue = []
#     indegree = defaultdict(list)
#     adjacent = defaultdict(list)

#     for source, destination in lst:
#         adjacent[source].append(destination)
#         indegree[destination].append(source)

#     # find all vertexes that have indgree equal to 0
#     for i in range(1, n + 1):
#         if len(indegree[i]) == 0:
#             queue.append(i)

#     while queue:
#         top = queue.pop(0)
#         result.append(top)
#         # remove edges from top to its neighbors
#         for vertex in adjacent[top]:
#             indegree[vertex].remove(top)
#             if len(indegree[vertex]) == 0:
#                 queue.append(vertex)

#     print(result)
#     return result
    
# lst = [[1,2], [1,3], [2,4], [2,10], [3,5], [4,8], [4, 6], [5,8], [6,3], [7,5], [7,9], [9,4], [9, 10] ]
# main(10, lst)

import random

# def kClosest(points, K):
#         dist = lambda i: points[i][0]**2 + points[i][1]**2

#         def sort(i, j, K):
#             # Partially sorts A[i:j+1] so the first K elements are
#             # the smallest K elements.
#             if i >= j: return

#             # Put random element as A[i] - this is the pivot
#             k = random.randint(i, j)
#             points[i], points[k] = points[k], points[i]

#             mid = partition(i, j)
#             if K < mid - i + 1:
#                 sort(i, mid - 1, K)
#             elif K > mid - i + 1:
#                 sort(mid + 1, j, K - (mid - i + 1))

#         def partition(i, j):
#             # Partition by pivot A[i], returning an index mid
#             # such that A[i] <= A[mid] <= A[j] for i < mid < j.
#             oi = i
#             pivot = dist(i)
#             i += 1

#             while True:
#                 while i < j and dist(i) < pivot:
#                     i += 1
#                 while i <= j and dist(j) >= pivot:
#                     j -= 1
#                 if i >= j: break
#                 points[i], points[j] = points[j], points[i]

#             points[oi], points[j] = points[j], points[oi]
#             return j

#         sort(0, len(points) - 1, K)
#         return points[:K]

# lst = [[1,2], [1,3], [2,4], [2,10], [3,5], [4,8], [4, 6], [5,8], [6,3], [7,5], [7,9], [9,4], [9, 10], [0,0] ]
# print(kClosest(lst, 5))

# def partition(lst, low, high):
#     pivot = lst[high]
#     buffer = low
#     for idx in range(low, high):
#         if lst[idx] < pivot :
#             lst[buffer], lst[idx] = lst[idx], lst[buffer]
#             buffer += 1

#     lst[buffer], lst[high] = lst[high], lst[buffer]
#     return buffer

# def quickSort(lst, low, high):
#     if low < high:
#         pivot = partition(lst, low, high)
#         quickSort(lst, low, pivot-1)
#         quickSort(lst, pivot+1, high)

# lst = [9,3,4,5,6,3,44,245,0,-434,324,333]
# quickSort(lst, 0, len(lst)-1)
# print(lst)

# def firstK(lst,low, high, K):
#     if K > len(lst) or K == 0: return []
#     if low < high: 
#         pivot = partition(lst, low, high)
#         if K <= pivot + 1:
#             firstK(lst, low, pivot-1, K)
#         elif K > pivot + 1:
#             firstK(lst, pivot+1, high, K - ((pivot-low) + 1) )

# def partition(lst, low, high):
#     pivot = lst[high]
#     buffer = low
#     for i in range(low, high):
#         if lst[i] < pivot:
#             lst[i], lst[buffer] = lst[buffer], lst[i]
#             buffer += 1
#     lst[high], lst[buffer] = lst[buffer], lst[high]
#     return buffer
    
# lst = [9,2,-9]

# test = lst + []

# k = 10
# print(lst)
# firstK(lst, 0, len(lst)-1, k)
# print(lst)
# print('------------')
# print(lst[:k])
# print('------------')
# test.sort()
# print(test[:k])
