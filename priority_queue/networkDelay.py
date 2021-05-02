# https://leetcode.com/problems/network-delay-time/solution/

from queue import PriorityQueue
from collections import defaultdict


class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        q = PriorityQueue()
        
        children = defaultdict(list)
        for element in times:
            children[element[0]].append((element[1],element[2]))
            
        q.put((0, k))
        
        max_distance = -1
        
        while not q.empty():
            priority, node = q.get()
            if node in visited:
                continue
            visited.add(node)
            if priority > max_distance:
                max_distance = priority
            for child in children[node]:
                q.put((child[1] + priority, child[0]))

        if len(visited) != n:
            return -1
        return max_distance