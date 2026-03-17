#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def findPeakElement(self , nums: List[int]) -> int:
        # write code here
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1
        # 0->1: up tendency
        # N-1->N-2: up tendency
        pos = [-1]
        self.bisection(nums, 0, len(nums)-1, pos)
        return pos[0]

    def bisection(self, arr:List[int], L:int, R:int, pos:List[int]):
        # both L and R have "up" tendency ([L-1]<[L] && [R]>[R+1])
        if R - L <= 0:
            return
        if pos[0] != -1:
            return
        if R - L == 1:
            pos[0] = R if arr[L] < arr[R] else L
            return
        mid = L + ((R-L)>>1)
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            pos[0] = mid
            return
        if arr[mid] > arr[mid+1]:
            self.bisection(arr, L, mid, pos)
        elif arr[mid] > arr[mid-1]:
            self.bisection(arr, mid, R, pos)
        
        
        
