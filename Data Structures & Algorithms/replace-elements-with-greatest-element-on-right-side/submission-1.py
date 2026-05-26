class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1
        ans = [0] * len(arr)
        for i in range(len(arr)-1 ,-1,-1):
            ans[i] = max_num
            if arr[i] > max_num:
                max_num = arr[i]
        return ans
