from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        # Sort logs by time
        logs.sort(key=lambda item: item[1])
        
        # Sort queries while preserving original indices
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        active_counts = defaultdict(int)
        
        left = 0
        right = 0
        m = len(logs)
        
        for original_idx, q_time in sorted_queries:
            window_start = q_time - x
            window_end = q_time
            
            # Expand right pointer: include logs with time <= window_end
            while right < m and logs[right][1] <= window_end:
                server_id = logs[right][0]
                active_counts[server_id] += 1
                right += 1
                
            # Shrink left pointer: remove logs with time < window_start
            while left < m and logs[left][1] < window_start:
                server_id = logs[left][0]
                active_counts[server_id] -= 1
                if active_counts[server_id] == 0:
                    del active_counts[server_id]
                left += 1
                
            # Total servers minus active servers gives idle servers
            ans[original_idx] = n - len(active_counts)
            
        return ans