#双指针法中的快慢指针法
class Solution:
    def removeDuplicates(self, nums) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow = slow+1
                nums[slow] = nums[fast]
            fast = fast + 1
        return slow+1


# '''我的代码解决不了有三个一样的情况，只解决的了有两个的情况'''
# class Solution:
#     def removeDuplicates(self, nums):
#         a =[]
#         for i in range(len(nums)):
#             if i == len(nums):
#                 break
#             if nums[i] in nums[i+1:]:
#                 a.append(nums[i+1:].index(nums[i])+i+1)
#                 for j in a:
#                     del nums[j]
#             else: continue
#         return len(nums)

a= Solution()
a.removeDuplicates([1,1,1,2,3,4,1])
# List_a = list(range(10))
# print(List_a)
# for i in range(len(List_a)-1,-1,-1):
#     if List_a[i]%2 == 0:
#         del List_a[i]
# print (List_a)
