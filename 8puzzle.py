#8puzzle

import copy
from heapq import heappush, heappop

n = 3
rows = [1, 0, -1, 0]
cols = [0, -1, 0, 1]


class PriorityQueue:

    def __init__(self):
        self.heap = []

    def push(self, key):
        heappush(self.heap, key)

    def pop(self):
        return heappop(self.heap)

    def empty(self):
        return not self.heap


class Node:

    def __init__(self, parent, mats, empty_tile_posi, costs, levels):
        self.parent = parent
        self.mats = mats
        self.empty_tile_posi = empty_tile_posi
        self.costs = costs
        self.levels = levels

    def __lt__(self, nxt):
        return (self.costs + self.levels) < (nxt.costs + nxt.levels)

    def calculateCosts(mats, final):
        count = 0
        for i in range(n):
            for j in range(n):
                if mats[i][j] != 0 and mats[i][j] != final[i][j]:
                    count += 1
        return count

    def newNodes(mats, empty_tile_posi, new_empty_tile_posi, levels, parent,
                 final):
        new_mats = copy.deepcopy(mats)
        x1, y1 = empty_tile_posi
        x2, y2 = new_empty_tile_posi
        new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]
        costs = Node.calculateCosts(new_mats, final)
        return Node(parent, new_mats, new_empty_tile_posi, costs, levels)

    def printMatrix(mats):
        for row in mats:
            print(" ".join(map(str, row)))
        print()

    def isSafe(x, y):
        return 0 <= x < n and 0 <= y < n

    def printPath(root):
        if root is None:
            return
        Node.printPath(root.parent)
        Node.printMatrix(root.mats)


def solve(initial, empty_tile_posi, final):
    pq = PriorityQueue()
    costs = Node.calculateCosts(initial, final)
    root = Node(None, initial, empty_tile_posi, costs, 0)
    pq.push(root)
    while not pq.empty():
        minimum = pq.pop()
        if minimum.costs == 0:
            Node.printPath(minimum)
            return
        # Generating all feasible children
        for i in range(4):
            new_tile_posi = [
                minimum.empty_tile_posi[0] + rows[i],
                minimum.empty_tile_posi[1] + cols[i]
            ]
            if Node.isSafe(new_tile_posi[0], new_tile_posi[1]):
                child = Node.newNodes(minimum.mats, minimum.empty_tile_posi,
                                      new_tile_posi, minimum.levels + 1,
                                      minimum, final)
                pq.push(child)


# Main Code
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
empty_tile_posi = [1, 2]
# Method call for solving the puzzle
solve(initial, empty_tile_posi, final)
