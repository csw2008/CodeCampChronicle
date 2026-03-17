#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def minNumberInRotateArray(self , nums: List[int]) -> int:
        # write code here
        if not nums:
            return -1
        return self.bisection(nums, 0, len(nums) - 1)

    def bisection(self, arr: List[int], L: int, R: int) -> int:
        if L == R:
            return arr[L]
            
        mid = L + ((R - L) >> 1)
        
        # only compare arr[mid] and arr[R]
        if arr[mid] > arr[R]:
            return self.bisection(arr, mid + 1, R)
        elif arr[mid] < arr[R]:
            return self.bisection(arr, L, mid)
        else:
            return self.bisection(arr, L, R - 1)

