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

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node (PriorityQueue - Min-Heap)
        frontier = PriorityQueueFrontier()
        f_root = root.cost + heuristic(root.state, grid.end)
        frontier.add(root, priority=f_root)
        
        # Search loop
        while True:
            # Check if frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)
        
            # Pop the node with the lowest priority f(n)
            c_n = frontier.pop()

            # Apply objective test when popping (essential for A* optimality)
            if grid.objective_test(c_n.state):
                return Solution(c_n, reached)
            
            # Explore valid successor actions
            for action in grid.actions(c_n.state):
                successor = grid.result(c_n.state, action)
                new_cost = c_n.cost + grid.individual_cost(c_n.state, action)
                
                # If the state has not been reached or we found a cheaper path to it
                if successor not in reached or new_cost < reached[successor]:
                    new_node = Node(
                        value="",
                        state=successor,
                        cost=new_cost,
                        parent=c_n,
                        action=action,
                    )

                    # Update reached with the lowest cost found
                    reached[successor] = new_cost

                    # Priority: f(n) = g(n) + h(n)
                    priority = new_cost + heuristic(successor, grid.end)
                    frontier.add(new_node, priority=priority) 
                   
        return NoSolution(reached)
