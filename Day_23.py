'''
這道題目曾出現在 Amazon 的面試中。

給定一個 integer array，從中找出 shortest unsorted subarray，並 return 其長度。若我們將該 unsorted subarray 由小到大排序，則整個 array 會變成 sorted array。

若原 array 是 sorted array，則 shortest unsorted subarray 的長度為 0
Example 1:

Input: nums = [1, 6, 3, 8, 10, 9, 10, 20]
Output: 5
Explanation: Shortest subarray 為 [6, 3, 8, 10, 9]，將此 subarray 由小到大排序以後，原本的 array 就會是 sorted array
Example 2:

Input: nums = [-3, -1, 3, 4, 10]
Output: 0
Explanation: nums 本身是 sorted array，所以 shortest unsorted subarray 長度為 0
Function Signature
class Solution:

    # @param nums: List[int]
    # @return int
    def findShortestUnsortedSubarray(self, nums):
        # Implement me
'''