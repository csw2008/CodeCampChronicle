#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @param target int整型 
# @return int整型
#
class Solution:
    def search(self , nums: List[int], target: int) -> int:
        # write code here
        finished = [False, -1]
        self.bisection(nums, 0, len(nums)-1, target, finished)
        return finished[1]
    
    def bisection(self, arr:List[int], L:int, R:int, target:int, finished:List):
        if finished[0] == True:
            return
        if L >= R:
            if L == R and arr[L] == target:
                finished[0] = True
                finished[1] = L
            return
        mid = L + ((R-L)>>1)
        self.bisection(arr, L, mid, target, finished)
        self.bisection(arr, mid+1, R, target, finished)

