from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        frontier = PriorityQueueFrontier()
        frontier.add(root, grid.manhattan_distance(root.state))

        while True:
            # Check if frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            n = frontier.pop()

            if grid.objective_test(n.state):
                return Solution(n, reached)

            for action in grid.actions(n.state):
                successor = grid.result(n.state, action)
                successor_cost = n.cost + grid.individual_cost(n.state, action)

                if successor not in reached or successor_cost < reached[successor]:
                    new_node = Node(
                        "",
                        state = successor,
                        cost = successor_cost,
                        parent = n,
                        action = action
                    )
                    reached[successor] = successor_cost
                    frontier.add(new_node, grid.manhattan_distance(new_node.state))

        return NoSolution(reached)
