#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型
#
class Solution:
    def InversePairs(self , nums: List[int]) -> int:
        # write code here
        if len(nums) <= 1:
            return 0
        return self.mergeSort(nums, 0, len(nums)-1) % 1000000007

    def mergeSort(self, arr:List[int], L:int, R:int) -> int:
        if L >= R:
            return 0
        mid = L + ((R-L) >> 1)
        return self.mergeSort(arr, L, mid) + self.mergeSort(arr, mid+1, R) + self.merge(arr, L, mid, R)
    
    def merge(self, arr:List[int], L:int, mid:int, R:int) -> int:
        if L >= R:
            return 0
        left = L
        right = mid + 1
        # index = 0
        ass = []
        num = 0
        while left <= mid and right <= R:
            if arr[left] > arr[right]:
                num += R-right+1
                ass.append(arr[left])
                left += 1
            else:
                ass.append(arr[right])
                right += 1
        ass.extend(arr[left:mid+1])
        ass.extend(arr[right:R+1])
        arr[L:R+1] = ass[:]
        return num
