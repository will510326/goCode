"""
這道題目的簡化版曾出現在 Google 的面試中。

給定一個整數陣列 nums，從中找出總和最大且長度最長的 subarray，並 return 這個 subarray。若存在多個符合條件的 subarray，return 其中任一個即可。

Subarray 為 nums 中連續的元素所組成的 array，其最小長度為 1
Subarray 的總和的定義為該 subarray 中，所有元素的和
Subarray 的長度定義為該 subarray 的元素個數
時間複雜度要求為 O(n)，其中 n = len(nums)
Constraints:

n = len(nums) >= 1
Example 1:

Input: nums = [3, -1, 3, -1, -5, 5, -1, -9]
Output: [3, -1, 3]
Explanation: 
Subarray [3, -1, 3] 的和為 5，長度為 3，是 nums 中擁有最大總和且長度最長的 subarray。
Subarray [5] 也是總和為 5 的 subarray，但長度只有 1。
Example 2:

Input: nums = [-200, 100, -100, 200, -200, 200, -300]
Output: [100, -100, 200, -200, 200]
Explanation: 
Subarray [100, -100, 200, -200, 200] 的和為 200，長度為 5，是 nums 中擁有最大總和且長度最長的 subarray。
Subarray [200] 和 [200, -200, 200] 也是總和為 200 的 subarray，但長度分別只有 1 和 3。
Function Signature
class Solution:

    # @param nums: List[int]
    # @return List[int]
    def longestMaxSubarray(self, nums):
        # Implement me
"""

