class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = timer = 0 
        for g, p in sorted(zip(growTime, plantTime), reverse=True):
            timer += p
            ans = max(ans, timer+g)
        return ans
        # cur_plant_time = 0
        # result = 0
        # indices = sorted(range(len(plantTime)), key=lambda x: -growTime[x]) 
        # for i in indices:
        #     cur_plant_time += plantTime[i]
        #     result = max(result, cur_plant_time + growTime[i])
        # return result