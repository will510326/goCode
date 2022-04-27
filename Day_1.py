'''
這道題目曾出現在 Apple 的面試中。

給定一個由小至大排序過的陣列 nums，以及一個整數 target，找出此 target 適當的插入點 (index)，使陣列維持由小至大的排序，並返回其 index。

若有多個可能的 index，需 return 最小的 index
時間複雜度要求為 O(logn)

Example 1:

Input: nums = [1, 3, 5, 7, 9], target = 6
Output: 3
Explanation: 6 的插入點為 5 和 7 之間，而此插入點的 index 為 3。

Example 2:

Input: nums = [1, 3, 3, 3, 3], target = 3
Output: 1
Explanation: 3 的插入點為 1 和 3 之間，而此插入點的 index  為 1
Function Signature

class Solution:

    # @param nums: List[int]
    # @param target: int
    # @return int
    def searchInsertionPosition(self, nums, target):
        # Implement me
'''

class Solution():
    def searchInsertionPosition(self, nums, target):
        datas = []
        for i, v in enumerate(nums):
            if v < target:
                datas.append(v)
        nums_1 = nums[len(datas):]
        datas.append(target)
        datas.index(target)
        datas.extend(nums_1)
        return datas.index(target)
a = Solution()

nums =  [1, 3, 5, 7, 9]
target = 6
print(a.searchInsertionPosition(nums,target))
