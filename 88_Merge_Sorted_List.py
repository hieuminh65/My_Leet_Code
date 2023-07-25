def merge(nums1, m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1 
        pW = m+n - 1
        # 7 8 9 0 0 0 
        # 1 2 3
        while p1 >= 0 and p2 >=0:
            if nums1[p1] > nums2[p2]:
                nums1[pW] = nums1[p1]
                p1-=1
            else:
                nums1[pW] = nums2[p2]
                p2-=1
            pW-=1
        print(p1, p2, pW)
        print(nums1)
        while p1 >= 0:
            nums1[pW] = nums1[p1]
            p1-=1
            pW-=1
        while p2 >= 0:
            nums1[pW] = nums2[p2]
            p2-=1
            pW-=1


        return nums1

print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
