def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            elif nums[0] == 0:
                return 1
        else:
            nums.sort()
        last = len(nums)
        
        if last != nums[-1]:
            return last
        elif nums[0] != 0:
            return 0
        else:
            for i in range(0,len(nums)-1):
                if nums[i] != nums[i+1] - 1:
                    return nums[i] + 1