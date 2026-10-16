from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()
        
        print(f"\n--- INICIO BÚSQUEDA DFS ---")
        print(f"Punto de partida: {root.state} | Meta: {grid.end}")

        # Apply objective test to root node
        if grid.objective_test(root.state):
            return Solution(root, expanded)
        
        
        # Initialize frontier with the root node (Stack - LIFO)
        frontier=StackFrontier()
        frontier.add(root)
        
        #Search loop
        while True:
            # Check if frontier is empty
            if frontier.is_empty():
                print("Frontier is empty: NO SOLUTION FOUND.")
                return NoSolution(expanded)
            
            # Pop the current node from the stack
            c_n=frontier.remove()
                        
            # Skip if already expanded
            if c_n.state in expanded:
                continue
            
            # Mark state as expanded
            expanded[c_n.state]=c_n
            
            # Explore valid successor actions
            for action in grid.actions(c_n.state):
                successor = grid.result(c_n.state, action)

                # Skip if already expanded
                if successor not in expanded:
                    new_node = Node(
                        value= "",
                        state = successor,
                        cost = c_n.cost + grid.individual_cost(c_n.state, action),
                        parent = c_n,
                        action=action
                        )
                    
                    # Apply objective test
                    if grid.objective_test(new_node.state):
                        print(f"\n GOAL FOUND at {new_node.state}")
                        expanded[new_node.state] = new_node
                        return Solution(new_node, expanded)
                    
                    frontier.add(new_node)
                    
        return NoSolution(expanded)
