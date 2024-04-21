'''

# -*- coding: utf-8 -*-

# - Author    : Tianyu Wang
# - Email     : tywang22@m.fudan.edu.cn
# - Date      : ...

# - Desciption: LeetCode 面试经典150题 数组 / 字符串部分

'''
    
from typing import List

####################################### 88. 合并两个有序数组 #######################################

# # 类定义
# # S1 套接后排序
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
#         nums1[m:] = nums2
#         nums1.sort()

# # 指针 -> 两个非递减数组
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         sorted = []
#         p1, p2 = 0, 0
#         while p1 < m or p2 < n:
#             if p1 == m:
#                 sorted.append(nums2[p2])
#                 p2 += 1
#             elif p2 == n:
#                 sorted.append(nums1[p1])
#                 p1 += 1
#             elif nums1[p1] < nums2[p2]:
#                 sorted.append(nums1[p1])
#                 p1 += 1
#             else:
#                 sorted.append(nums2[p2])
#                 p2 += 1
#         nums1[:] = sorted

# # 测试用例
# test_cases = [
#     ([[1,2,3,0,0,0], 3, [2,5,6], 3], [1,2,2,3,5,6]),
#     ([[1], 1, [], 0], [1]),
#     ([[0], 0, [1], 1], [1]),
#     # 更多测试用例...
# ]

# # 驱动代码
# if __name__ == "__main__":
#     solution = Solution()
#     for i, (params, expected) in enumerate(test_cases):
#         solution.merge(*params)  # 使用*来解包参数列表
#         result = params[0]
#         # print(result)
#         assert result == expected, f"案例{i + 1}失败：期望{expected}，得到{result}"
#         print(f"案例{i + 1}成功。")

####################################### 189. 轮转数组 #######################################

# # 类定义
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)

#         k %= n # 处理超出列表长度的情况

#         nums[:] = nums[-k:] + nums[:-k] # 切片融合


# # 测试用例
# test_cases = [
#     ([[-1, -100, 3, 99], 2], [3,99,-1,-100]),
#     ([[-1, -100, 3, 99], 1], [99,-1,-100,3]),
#     # 更多测试用例...
# ]

# # 驱动代码
# if __name__ == "__main__":
#     solution = Solution()
#     for i, (params, expected) in enumerate(test_cases):
#         solution.rotate(*params)  # 使用*来解包参数列表
#         result = params[0]
#         # print(result)
#         assert result == expected, f"案例{i + 1}失败：期望{expected}，得到{result}"
#         print(f"案例{i + 1}成功。")

####################################### 66. 加一 #######################################

# # 类定义
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits)-1, -1, -1):
#             if digits[i] != 9:
#                 digits[i] += 1
#                 return digits
#             else:
#                 if i != 0:
#                     digits[i] = 0
#                 else:
#                     digits[i] = 1
#                     digits.append(0)
#                     return digits


# # 测试用例
# test_cases = [
#     ([1,2,3], [1,2,4]),
#     ([4,3,2,1], [4,3,2,2]),
#     ([0], [1]),
#     # 更多测试用例...
# ]

# # 驱动代码
# if __name__ == "__main__":
#     solution = Solution()
#     for i, (params, expected) in enumerate(test_cases):
#         # result = solution.plusOne(*params)  # 使用*来解包参数列表
#         result = solution.plusOne(params)
#         # print(result)
#         assert result == expected, f"案例{i + 1}失败：期望{expected}，得到{result}"
#         print(f"案例{i + 1}成功。")

# ####################################### 724. 寻找数组的中心下标 #######################################

# # 类定义
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         # sum
#         sum = 0
#         for i in range(len(nums)):
#             sum += nums[i]

#         # part
#         part = 0
#         for i in range(len(nums)):
#             if part == (sum-nums[i]-part):
#                 return i
#             part += nums[i]
        
#         # none
#         return -1


# # 测试用例
# test_cases = [
#     ([1, 7, 3, 6, 5, 6], 3),
#     ([1,2,3], -1),
#     ([2,1,-1], 0),
#     # 更多测试用例...
# ]

# # 驱动代码
# if __name__ == "__main__":
#     solution = Solution()
#     for i, (params, expected) in enumerate(test_cases):
#         # result = solution.plusOne(*params)  # 使用*来解包参数列表
#         result = solution.pivotIndex(params)
#         # print(result)
#         assert result == expected, f"案例{i + 1}失败：期望{expected}，得到{result}"
#         print(f"案例{i + 1}成功。")

####################################### 485. 最大连续 1 的个数 #######################################

