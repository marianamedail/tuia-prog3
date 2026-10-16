from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Apply objective test
        if grid.objective_test(root.state):
            return Solution(root, reached)

        frontier = QueueFrontier()
        frontier.add(root)


        print(f"reached: {reached}")

        # Initialize frontier with the root node
        while True:
            # Check if frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            n = frontier.remove()

            # print(f"Current node: {n.state}")

            for action in grid.actions(n.state):
                successor = grid.result(n.state, action)

            # print(f"Successor: {successor}")

                if successor not in reached:
                    new_node = Node(
                        "",
                        state = successor,
                        cost = n.cost + grid.individual_cost(n.state, action),
                        parent = n,
                    )

                    if grid.objective_test(new_node.state):
                        return Solution(new_node, reached)
                    reached[new_node.state] = True
                    frontier.add(new_node)

        return NoSolution(reached)

