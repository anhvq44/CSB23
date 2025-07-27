# Time/space complexity: O(n+m) where n and m is the length of nums1 and nums2
def CombineArrays(nums1, nums2):
    res = [0]*(len(nums1) + len(nums2))
    i = 0
    j = 0
    k = 0
    
    while (i<len(nums1)) and (j<len(nums2)):
        if nums2[j] < nums1[i]:
            res[k] = nums2[j]
            j += 1
        else:
            res[k] = nums1[i]
            i += 1
        k += 1
    
    while i<len(nums1):
        res[k] = nums1[i]
        i += 1
        k += 1
    while j<len(nums2):
        res[k] = nums2[j]
        j += 1
        k += 1
    
    return res

print(CombineArrays([2, 5, 6], [1, 2, 3]))