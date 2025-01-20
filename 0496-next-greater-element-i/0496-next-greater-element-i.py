class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        # Create a stack to keep track of the elements whose next greater element is not found yet
        stack = []
        for num in nums2:
            # While the stack is not empty and the current number is greater than the top element in the stack
            while stack and num > stack[-1]:
                # Pop the top element from the stack and set its next greater element to the current number
                next_greater[stack.pop()] = num
            # Add the current number to the stack
            stack.append(num)
        result = []
        for num in nums1:
            # If the next greater element of the current number is found
            if num in next_greater:
                result.append(next_greater[num])
            else:
                result.append(-1)
        return result