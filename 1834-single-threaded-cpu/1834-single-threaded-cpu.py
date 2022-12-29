class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(start,dur,i) for i,(start,dur) in enumerate(tasks)],reverse=True)
        
        next_available_t = 0
        queued_tasks = []
        
        res = []
        # start, dur, id
        while queued_tasks or tasks:
            # start or gap between tasks
            if not queued_tasks and next_available_t <= tasks[-1][0]:
                next_available_t = tasks[-1][0]
        
            # queue 'expired tasks'
            while tasks and tasks[-1][0] <= next_available_t:
                start,dur,id = tasks.pop()
                heappush(queued_tasks, (dur, id))
            
            dur,id = heappop(queued_tasks)
            next_available_t += dur
            res.append(id)
        
        return res
        