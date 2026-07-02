class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # l = 0
        # r = l+1

        for l, n in enumerate(numbers):
            r = l + 1
            while r < len(numbers):
                if (numbers[l] + numbers[r]) == target:
                    return [l+1, r+1]
                r+=1
        




        