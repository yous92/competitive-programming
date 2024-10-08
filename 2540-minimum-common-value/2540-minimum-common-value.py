class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j= 0
        common = -1
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
                
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                common = nums1[i]
                break
        return common