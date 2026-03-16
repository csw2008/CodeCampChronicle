class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.Sorting(nums)
        ans = str("")
        for ele in nums:
            ans += str(ele)
        
        for i in range(len(ans)):
            if i == len(ans)-1 and ans[i] == '0':
                return "0"
            if ans[i] != '0':
                break
        ans = ans[i:]

        return ans
        
    def Sorting(self, arr:List[int]):
        from functools import cmp_to_key
        arr.sort(key=cmp_to_key(lambda x, y: -1 if str(x)+str(y) > str(y)+str(x) else 1), reverse=False)