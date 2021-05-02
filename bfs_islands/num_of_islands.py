def visit_island(root_node, grid, unvisited):
    q = [root_node]
    while q:
        node = q.pop(0)
        if node is root_node or node in unvisited:
            if node is not root_node:
                unvisited.remove(node)
            if node[0] + 1 < len(grid):
                if grid[node[0] + 1][node[1]] == "1":
                    q.append((node[0] + 1, node[1]))
            if node[0] - 1  >= 0:
                if grid[node[0] - 1][node[1]] == "1":
                    q.append((node[0] - 1, node[1]))
            if node[1] - 1  >= 0:
                if grid[node[0]][node[1] - 1] == "1":
                    q.append((node[0], node[1] - 1))
            if node[1] + 1  < len(grid[0]):
                if grid[node[0]][node[1] + 1] == "1":
                    q.append((node[0], node[1] + 1))
    

def numIslands(grid: List[List[str]]) -> int:
    unvisited = { (x, y) for x in range(len(grid))
                         for y in range(len(grid[0])) }
    num_islands = 0
    while unvisited:
        node = unvisited.pop()
        if grid[node[0]][node[1]] == "1":            
            visit_island(node, grid, unvisited)
            num_islands += 1           
    return num_islands


grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
assert numIslands(grid) == 1