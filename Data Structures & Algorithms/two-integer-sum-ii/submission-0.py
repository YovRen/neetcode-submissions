class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #1. 用一个字典「数字：下标」加到里面
        dicts = {}
        for i in range(len(numbers)):
            if target-numbers[i] in dicts:
                return [dicts[target-numbers[i]]+1,i+1]
            else:
                dicts[numbers[i]] = i 