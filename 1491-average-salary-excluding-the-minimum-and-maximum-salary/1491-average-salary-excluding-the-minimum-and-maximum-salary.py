class Solution:
    def average(self, salary: List[int]) -> float:
        mx = max(salary)
        mn = min(salary)
        return (sum(salary) - (mx + mn))/(len(salary) -2)