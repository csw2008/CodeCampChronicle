class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.Sorting(intervals)

        ans = []
        nowleft = intervals[0][0]
        nowright = intervals[0][1]
        for pair in intervals:
            # pair: [left, right]
            if nowright < pair[0]:
                ans.append([nowleft,nowright])
                nowleft = pair[0]
                nowright = pair[1]
            elif nowright >= pair[0]: 
                # if pair[1] <= nowright:
                #     pass
                if pair[1] > nowright:
                    nowright = pair[1]
        ans.append([nowleft,nowright])
        return ans
        
    def Sorting(self, arr: List[List[int]]):
        arr.sort(key=lambda x: x[0], reverse=False)
