class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        f = s = 0
        while f < m and s < n:
            if nums1[f] <= nums2[s]:
                f += 1
            else:
                for i in range(m - 1, f - 1, -1):
                    nums1[i + 1] = nums1[i]
                nums1[f] = nums2[s]
                m += 1
                s += 1

        while s < n:
            nums1[m] = nums2[s]
            m += 1
            s += 1

        return nums1