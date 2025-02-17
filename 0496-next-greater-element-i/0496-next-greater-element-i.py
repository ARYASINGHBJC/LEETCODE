class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        seen = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                seen[stack.pop()] = num
            stack.append(num)
        for ele in stack:
            seen[ele] = -1
        return [seen[num] for num in nums1]
        