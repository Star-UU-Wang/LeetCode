'''

# -*- coding: utf-8 -*-

# - Author    : Tianyu Wang
# - Email     : tywang22@m.fudan.edu.cn
# - Date      : ...

# - Desciption: LeetCode 面试经典150题 数组 / 字符串部分

'''
    
from typing import List

####################################### 88. 合并两个有序数组 #######################################

# 类定义

# S1 套接后排序
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        nums1[m:] = nums2
        nums1.sort()

# S1 套接后排序
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        nums1[m:] = nums2
        nums1.sort()

# 指针 -> 两个非递减数组
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted


# 测试用例
test_cases = [
    ([[1,2,3,0,0,0], 3, [2,5,6], 3], [1,2,2,3,5,6]),
    ([[1], 1, [], 0], [1]),
    ([[0], 0, [1], 1], [1]),
    # 更多测试用例...
]


# 驱动代码
if __name__ == "__main__":
    solution = Solution()
    for i, (params, expected) in enumerate(test_cases):
        solution.merge(*params)  # 使用*来解包参数列表
        result = params[0]
        # print(result)
        assert result == expected, f"案例{i + 1}失败：期望{expected}，得到{result}"
        print(f"案例{i + 1}成功。")