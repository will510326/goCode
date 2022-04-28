'''
- goCode 趣刷題

這道題目曾出現在 Apple 的面試中。

實作一個 time-based key-value store 的 class Store 中的兩個 methods:

set(key, value, timestamp)
Input: key -> str, value -> str, timestamp -> int
Output: None
將給定的 key-value pair 儲存到 Store 中，並記錄該筆資料所發生的時間 (timestamp)
get(key, timestamp)
Input: key -> str, timestamp -> int
Output: int
根據給定的 timestamp，return 等於或小於此 timestamp 的時間，該 key 被存入的值
若有多筆資料其存入的時間均小於給定的 timestamp，則 return 最接近此 timestamp，key 所對應的值
若 key 不存在，則 return 空字串 ""
若給定的 timestamp 小於該 key 所有時間紀錄，則 return 空字串 ""
Constraints:

Test case 中，呼叫 set method 的 timestamp 是嚴格遞增的
Example:

Input:
 1  store = Store()
 2  store.set("stock", "low", 10)
 3  store.set("ETF", "high", 15)
 4  store.set("stock", "high", 20)
 5  store.get("stock", 3)
 6  store.get("stock", 10)
 7  store.get("ETF", 11)
 8  store.get("stock", 15)
 9  store.get("ETF", 15)
10  store.get("stock", 20)
11  store.get("stock", 25)

Output:
 5    ""        # 由於 "stock" 沒有時間小於等於 3 的資料，所以 return 空字串
 6    "low"     # 時間小於等於 10 的 "stock" 的資料為 "low"
 7    ""        # 由於 "ETF" 沒有時間小於等於 11 的資料，所以 return 空字串
 8    "low"     # 時間小於等於 15 的 "stock" 的資料為 "low"
 9    "high"    # 時間小於等於 15 的 "ETF" 的資料為 "high"
10    "high"    # 時間小於等於 20 的 "stock" 的資料為 "high"
11    "high"    # 時間小於等於 25 的 "stock" 的資料為 "high"
Function Signature
class Store:

    def __init__(self):
        # Implement me if necessary

    # @param key: str
    # @param value: str
    # @param timestamp: int
    # @return None
    def set(self, key, value, timestamp):
        # Implement me

    # @param key: str
    # @param timestamp: int
    # @return str
    def get(self, key, timestamp):
        # Implement me
'''