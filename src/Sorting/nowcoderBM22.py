#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 比较版本号
# @param version1 string字符串 
# @param version2 string字符串 
# @return int整型
#
class Solution:
    def compare(self , version1: str, version2: str) -> int:
        # write code here
        sv1 = version1.split(".")
        sv2 = version2.split(".")
        v1 = []
        v2 = []
        for ele in sv1:
            v1.append(int(ele))
        for ele in sv2:
            v2.append(int(ele))
        len1 = len(v1)
        len2 = len(v2)
        if len1 > len2:
            for i in range(len1-len2):
                v2.append(0)
        elif len1 < len2:
            for i in range(len2-len1):
                v1.append(0)
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0