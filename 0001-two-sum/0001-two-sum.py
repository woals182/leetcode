class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_dict = {}
        
        for idx, num in enumerate(nums):
            
            need_number = target - num

            if need_number in number_dict:
                return [number_dict[need_number], idx]
            
            number_dict[num] = idx

