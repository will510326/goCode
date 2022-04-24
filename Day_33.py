'''
這道題目曾出現在 Goldman Sachs 的面試中。

給定一個 N-by-N matrix friends，friends[i][j] = 1 代表 i 和 j 是朋友，friends[i][j] = 0 代表 i 和 j 不是朋友。若 i 和 j 是朋友，且 j 和 k 是朋友，則 i 和 k 也是朋友，ijk 三人可形成一個朋友圈 (Friend Circles)。根據此定義，找出給定的 friends matrix 中，總共有多少個獨立的朋友圈。

兩個朋友圈若有交集，則視為同一個朋友圈；若無交集，則為 2 個獨立的朋友圈
Example:

Input: friends = 
    [
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 1]
    ]
Output: 2
Explanation: 共有 2 個朋友圈: [0, 1, 3] 及 [2]，所以 return 2
Function Signature
class Solution:
    
    # @param friends: List[List[int]]
    # @return int
    def countFriendCircles(self, friends):
        # Implement me
'''