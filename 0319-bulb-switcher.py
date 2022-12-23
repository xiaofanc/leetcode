"""
假设有6盏灯，只看第6盏灯，结束时说明状态？
6 = 1x6 = 2x3 -> 被按4次，关了

假设有16盏灯，只看第16盏灯：
16 = 1x16 = 2x8 = 4x4 -> 被按5次，开着
所以最后有1x1=1, 2x2=4, 3x3=9, 4x4=16 被按奇数次，开着
"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))