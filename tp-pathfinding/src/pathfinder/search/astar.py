from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        root_estimated_total_cost = root.cost + grid.manhattan_distance(root.state)
        frontier.add(root, root_estimated_total_cost)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

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
                    new_node_estimated_total_cost = new_node.cost + grid.manhattan_distance(new_node.state)
                    frontier.add(new_node, new_node_estimated_total_cost)

        return NoSolution(reached)
