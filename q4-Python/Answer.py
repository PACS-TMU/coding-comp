def intersection(nums1, nums2):
    result = []
    set_nums1 = set(nums1)

    for num in set_nums1:
        if num in nums2:
            result.append(num)
            nums2.remove(num)

    return result