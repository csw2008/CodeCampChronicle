class Solution:
    def reversePairs(self, record: List[int]) -> int:
        if len(record) <= 1:
            return 0
        N = len(record)
        num_up_pair = self.mergeSort(record, 0, N-1)
        return (int)(num_up_pair)

    def mergeSort(self, arr:List[int], L:int, R:int) -> int:
        if L >= R:
            return 0
        mid = L + ((R - L) >> 1)
        return self.mergeSort(arr, L, mid) + self.mergeSort(arr, mid+1, R) + self.merge(arr, L, mid, R)

    def merge(self, arr:List[int], L:int, mid:int, R:int) -> int: # big -> small (reverse)
        if L >= R:
            return 0
        # [L,mid] [mid+1,R]
        left = L 
        right = mid + 1
        num_up = 0
        assis = []
        while left <= mid and right <= R:
            if arr[left] > arr[right]:
                num_up += R - right + 1
                assis.append(arr[left])
                left += 1
            elif arr[left] == arr[right]:
                assis.append(arr[right])
                right += 1
            elif arr[left] < arr[right]:
                assis.append(arr[right])
                right += 1

        assis.extend(arr[left:mid+1])
        assis.extend(arr[right:R+1])
        arr[L:R+1] = assis[:]
        return num_up
    