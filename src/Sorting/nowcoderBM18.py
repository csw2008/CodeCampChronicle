# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param target int整型 
# @param array int整型二维数组 
# @return bool布尔型
#
class Solution:
    def Find(self , target: int, array: List[List[int]]) -> bool:
        # write code here
        # stand at right up or left buttom
        # eg. right up
        # row++: bigger than current value 
        # column--: less than current value
        rownum = len(array)
        columnnum = len(array[0])
        row = 0
        column = columnnum - 1
        while row <= rownum - 1 and column >= 0:
            if array[row][column] == target:
                return True
            elif array[row][column] > target:
                column -= 1
            else:
                row += 1
        return False

