class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2  # Find the middle of the array
            left_half = nums[:mid]  # Split the array into two halves
            right_half = nums[mid:]

            # Recursively sort both halves
            self.sortArray(left_half)
            self.sortArray(right_half)

            i = j = k = 0                                                                                                                                                                                                                                                     

            # Merge the sorted halves
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            # If any elements are left in either half, add them
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1

        return nums