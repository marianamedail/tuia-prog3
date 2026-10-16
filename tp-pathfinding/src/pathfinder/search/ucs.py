from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        while True:
            # Check if frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            n = frontier.pop()

            # Apply objective test
            if grid.objective_test(n.state):
                return Solution(n, reached)

            for action in grid.actions(n.state):
                successor = grid.result(n.state, action)
                successor_cost = n.cost + grid.individual_cost(n.state, action)

                print(f"Current node: {n.state}, Successor: {successor}, Cost: {successor_cost}")

                if successor not in reached or successor_cost < reached[successor]:
                    new_node = Node(
                        "",
                        state = successor,
                        cost = successor_cost,
                        parent = n,
                        action = action
                    )

                    reached[successor] = successor_cost
                    frontier.add(new_node, successor_cost)

        return NoSolution(reached)

'''
function GRAPH-UCS(problema) return solución o no-solución
    n₀ ← NODO(problema.estado-inicial, None, None, 0)
    frontera ← ColaPrioridad()
    frontera.encolar(n₀,n₀.costo)
    alcanzados ← {n₀.estado: n₀.costo}
    do
        if frontera.vacía() then return no-solución
        n ← frontera.desencolar()
        if problema.test-objetivo(n.estado) then return solución(n)
        forall a in problema.acciones(n.estado) do
            s’ ← problema.resultado(n.estado, a)
            c’ ← n.costo + problema.costo-individual(n.estado,a)
            if s’ is not in alcanzados or c’ < alcanzados[s’] then
                n’ ← Nodo(s’, n, a, c’)
                alcanzados[s’] ← c’

                frontera.encolar(n’,c’)
'''