class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1
        
        n1_q, n2_q = deque([(node1, 0)]), deque([(node2, 0)])
        n1_vis, n2_vis = {}, {} # node and length
        
        n1_vis[node1] = 0
        n2_vis[node2] = 0
        
        res_node = float('inf')
        res_length = float('inf')
        
        
        while n1_q or n2_q:
            if n1_q:
                node, dis = n1_q.popleft()
                neighbor = edges[node]
                if neighbor in n1_vis: continue
                if neighbor == -1: continue
                    
                if neighbor in n2_vis:
                    dis = max(dis + 1, n2_vis[neighbor])
                    if dis < res_length:
                        res_node = neighbor
                        res_length = dis
                    elif dis == res_length:
                        res_node = min(res_node, neighbor)
                    
                
                n1_vis[neighbor] = dis + 1
                n1_q.append((neighbor, dis + 1))
                
            if n2_q:
                node, dis = n2_q.popleft()
                neighbor = edges[node]
                if neighbor in n2_vis: continue
                if neighbor == -1: continue
                    
                if neighbor in n1_vis:
                    dis = max(dis + 1, n1_vis[neighbor])
                    if dis < res_length:
                        res_node = neighbor
                        res_length = dis
                    elif dis == res_length:
                        res_node = min(res_node, neighbor)
                    
                
                n2_vis[neighbor] = dis + 1
                n2_q.append((neighbor, dis + 1))
                
            
        return res_node if res_node != float('inf') else -1