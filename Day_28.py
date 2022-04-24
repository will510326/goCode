'''
Hey Wayne，你今天刷題了嗎？

今天的題目如下

建議使用你熟悉的編輯器

根據定義好的 Function Signature 實現功能

練習效果會更好哦！

若有需要，我們也有提供付費詳解

請點下方連結查看詳細資訊！

50 題精選
祝刷題愉快：）

​

- goCode 趣刷題

這道題目曾出現在 Google 的面試中。

破解一個擁有 n 位數密碼的保險箱。給定 startCode，targetCode，及一組會導致保險箱爆炸的密碼 badCodes，我們的任務是盡量減少旋轉密碼輪盤的次數，從 startCode 開始旋轉密碼輪盤，直到達到 targetCode 為止，就可以打開保險箱。最後 return 過程中密碼變化的歷史紀錄，若存在多種可能，return 一種即可。由於此保險箱有自我保護機制，若轉到 badCodes 中的密碼，保險箱就會爆炸導致任務失敗，所以我們必須避免這些會爆炸的密碼。

每個位數的密碼輪盤上的數字範圍是 0 到 9，共 10 個數字
每個位數只能向上或向下轉動 1 單位
0 -> 1 or 9, 1 -> 2 or 0, 2 -> 3 or 1, ..., 9 -> 0 or 8
每次只能轉動一個位數
若無法從 startCode 抵達 targetCode，return "" 即可
Constraints:

badCodes 不會包含 startCode 及 targetCode
startCode，targetCode，及 badCodes 中的所有密碼都會同時為 n 位數
1 <= n <= 10
Example 1:

Input: startCode = "1", targetCode = "3", badCodes = ["2"]
Output: "1->0->9->8->7->6->5->4->3"
Explanation: "1" 不能向上轉，因為會變成 "2"，而 "2" 會使保險箱爆炸
Example 2:

Input: startCode = "00", targetCode = "02", badCodes = ["01", "03", "12", "92"]
Output: ""
Explanation: 無法不經過 badCodes 而達到 "02"，所以 return empty string
Example 3:

Input: startCode = "0000", targetCode = "0002", badCodes = ["0001"]
Output: "0000->1000->1001->1002->0002"
Explanation: "0000->9000->9001->9002->0002", "0000->0100->0101->0102->0002", "0000->0010->0011->0012->0002" 等等，也都是可行的最短路徑
Function Signature
class Solution:

    # @param startCode: str
    # @param targetCode: str
    # @param badNodes: List[str]
    # @return str
    def crackSafe(self, startCode, targetCode, badCodes)
        # Implement me
'''