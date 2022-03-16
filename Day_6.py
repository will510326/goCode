"""
這道題目曾出現在 Google 的面試中。

給定一個整數陣列 nums，從中找出總和最大的 subarray，並 return 其總和。

Subarray 為 nums 中連續的元素所組成的 array，其最小長度為 1
Subarray 的總和的定義為該 subarray 中，所有元素的和
時間複雜度要求為 O(n)，其中 n = len(nums)
Constraints:

nums 的長度 >= 1
Example 1:

Input: nums = [3, -1, 3, -1, -5, 5, -1, -9]
Output: 5
Explanation: 總和最大的 subarray 包含 [3, -1, 3] 及 [5]，兩者的總和均為 5。
Example 2:

Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: 總和最大的 subarray 為 [4,-1,2,1]，其總和為 6。 
Function Signature
class Solution:

    # @param nums: List[int]
    # @return int
    def maxSubarraySum(self, nums):
        # Implement me
"""

