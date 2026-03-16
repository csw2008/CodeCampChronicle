class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        if k > len(nums):
            k = len(nums)
        k = len(nums) - k # kth min

        finished = [False, 0]
        self.quickSort(nums, k, finished, 0, len(nums)-1)
        
        return finished[1]

        
    def quickSort(self, arr:List[int], k:int, finished:List, L:int, R:int):
        if finished[0] == True:
            return
        if L >= R:
            if L == R and L == k: # note: not forget this
                finished[0] = True 
                finished[1] = arr[k]
            return
        
        import random
        pivot = random.randint(L, R) # [L, R]
        arr[pivot], arr[R] = arr[R], arr[pivot]
        left, right = self.partition(arr, k, finished, L, R)
        if left > k: 
            self.quickSort(arr, k, finished, L, left-1)
        elif right < k:
            self.quickSort(arr, k, finished, right+1, R)

    def partition(self, arr:List[int], k:int, finished:List, L:int, R:int) -> Tuple[int, int]:

        if L >= R:
            return
        less = L-1
        more = R 
        num = arr[R]
        index = L
        while index < more:
            if arr[index] < num:
                less += 1
                arr[less], arr[index] = arr[index], arr[less]
                index += 1
            elif arr[index] == num:
                index += 1
            else:
                more -= 1
                arr[more], arr[index] = arr[index], arr[more]
        arr[more], arr[R] = arr[R], arr[more]
        
        if less+1 <= k and k <= more:
            finished[0] = True
            finished[1] = arr[k]
        return less+1, more
         