# class Solution:
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             res = target-nums[i]
#             if res in nums[i+1:]:
#                 return [i, nums[i+1:].index(res)+i+1 ] # [i+1:] 以i+1这个点作为起点了也就是索引是0


import pdb

def calculate_sum(n):
    total = 0
    for i in range(n):
        pdb.set_trace()
        total += i
    return total

calculate_sum(5)
# 作者：啥都会一点的研究生 https://www.bilibili.com/read/cv23455046?spm_id_from=444.41.list.card_opus.click 出处：bilibili

'''
取值的时候，是左闭右开的
'''
# a = [1,2,3,4,5]
# print(a[1:3])# [2,3]
# print(a[1:].index(5)) # 找一个列表中的索引的，必须这个值是在这个列表中的 3
