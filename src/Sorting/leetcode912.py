class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # self.mergeSort(nums, 0, length-1)
        # self.quickSort(nums, 0, length-1)
        self.heapSort(nums, length)
        return nums
    
    # O(NlogN): mergeSort, quickSort, heapSort

    # mergeSort
    def mergeSort(self, arr: List[int], L: int, R: int):
        if L >= R:
            return
        mid = L + ((R - L) >> 1)
        self.mergeSort(arr, L, mid)
        self.mergeSort(arr, mid+1, R)
        self.merge(arr, L, mid, R)
    def merge(self, arr: List[int], L:int, mid:int, R:int):
        # [L, mid] [mid+1, R]
        left = L
        right = mid+1
        assis = []
        while left <= mid and right <= R:
            if arr[left] < arr[right]:
                assis.append(arr[left])
                left += 1
            else:
                assis.append(arr[right])
                right += 1
        # while left <= mid:
        #     assis.append(arr[left])
        #     left += 1
        # while right <= R:
        #     assis.append(arr[right])
        #     right += 1
        # index = 0
        # for i in range(L, R+1):
        #     arr[i] = assis[index]
        #     index += 1

        # pythonic：
        assis.extend(arr[left:mid+1])
        assis.extend(arr[right:R+1])
        arr[L:R+1]=assis
    
    # quickSort
    def quickSort(self, arr:List[int], L:int, R:int):
        if L >= R:
            return
        import random
        index = random.randint(L, R)
        arr[index], arr[R] = arr[R], arr[index]
        num = arr[R]
        equal_left, equal_right = self.partition(arr, L, R)
        self.quickSort(arr, L, equal_left-1)
        self.quickSort(arr, equal_right+1, R)

    def partition(self, arr:List[int], L:int, R:int) -> Tuple(int, int):
        # arr[R] is the pivot
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
            elif arr[index] > num:
                more -= 1
                arr[more], arr[index] = arr[index], arr[more]
        arr[R], arr[more] = arr[more], arr[R] # note: Do not forget this.
        return less+1, more
        
    # heapSort
    def heapSort(self, arr:List[int], heapSize:int):
        for i in range(heapSize, -1, -1):
            self.heapify(arr, i, heapSize)

        while heapSize > 0:
            arr[0], arr[heapSize-1] = arr[heapSize-1], arr[0]
            heapSize -= 1
            self.heapify(arr, 0, heapSize)
        


    def heapify(self, arr:List[int], index:int, heapSize:int):
        if heapSize == 0:
            return
        # heapify current element arr[index]:
        left = index*2 + 1
        right = index*2 + 2
        while left < heapSize: # arr[index] has a children now.
            maxi = right if right < heapSize and arr[left] < arr[right] else left
            if arr[maxi] <= arr[index]:
                break
            arr[maxi], arr[index] = arr[index], arr[maxi]
            index = maxi
            left = index * 2 + 1
            right = index * 2 + 2

        