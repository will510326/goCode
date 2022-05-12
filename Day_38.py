'''
這道題目曾出現在 Amazon 的面試中。

從給定的 words (list of strings) 中，return 出現頻率前 k 高的字串。

Output 需依據以下規則排序:
由頻率高往頻率低進行排序
若兩個字串頻率相同，則依照 alphabetical order 排序
Time complexity 要求為 O(nlogk)
Space complexity 要求為 O(n)
Constraints:

1 <= k < number of unique strings
所有字串均由小寫英文字母所組成
Example 1:

Input: words = ["google", "facebook", "amazon", "facebook", "google", "apple"], k = 2
Output: ["facebook", "google"]
Explanation:
    - 出現頻率為 { "google": 2, "facebook": 2, "amazon": 1, "apple": 1 }
    - 所以出現頻率前 2 高的兩個字串為 "google" 和 "facebook"
    - 將 "google" 和 "facebook" 以 alphabetical order 排序，所以 return ["facebook", "google"] 
Function Signature
class Solution:

    # @param words: List[str]
    # @param k: int
    # @return List[str]
    def findTopKFrequentWords(self, words, k):
        # Implement me
'''