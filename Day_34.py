'''
這道題目曾出現在 Facebook 的面試中。

給定一個 array of integers nums，找出 sum 為 k 的 subarray 的個數。

Subarray 的意思是某個 array 的子集，且必須由連續元素所組成
Example 1:

Input: nums = [-2, 2, 1, 0, -1], k = 0
Output: 4
Explanation: [-2, 2], [1, 0, -1], [0], [-2, 2, 1, 0, -1] 這四個 subarray 的 sum 均等於 k，所以 return 4
Function Signature
class Solution:

    # @param nums: List[int]
    # @param k: int
    # @return int
    def countSubarraySumEqualsK(self, nums, k):
        # Implement me
'''