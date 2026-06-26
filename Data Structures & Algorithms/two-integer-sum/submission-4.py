class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # 字典用来存储：{数字: 对应的索引}
        
        for i, num in enumerate(nums):
            complement = target - num  # 计算需要的另一个数字
            
            # 如果需要的数字已经在字典里了，直接返回它们的索引
            if complement in hash_map:
                return [hash_map[complement], i]
            
            # 如果不在，就把当前数字和索引存入字典，继续往后找
            hash_map[num] = i