# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                       , search.romania)
gz = search.GPSProblem('G', 'Z'
                       , search.romania)
nd = search.GPSProblem('N', 'D'
                       , search.romania)
mf = search.GPSProblem('M', 'F'
                       , search.romania)
print("Camino A-B:\n")
print("Búsqueda en anchura:")
print(search.breadth_first_graph_search(ab).path())
print("\nBúsqueda en profundidad:")
print(search.depth_first_graph_search(ab).path())
print("\nBranch and Bound:")
print(search.branch_and_bound_graph_search(ab).path())
print("\nBranch and Bound con subestimación:")
print(search.branch_and_bound_with_subestimation_graph_search(ab).path())
print("\n---------------------------------------------\n")
print("Camino O-E:\n")
print("Búsqueda en anchura:")
print(search.breadth_first_graph_search(oe).path())
print("\nBúsqueda en profundidad:")
print(search.depth_first_graph_search(oe).path())
print("\nBranch and Bound:")
print(search.branch_and_bound_graph_search(oe).path())
print("\nBranch and Bound con subestimación:")
print(search.branch_and_bound_with_subestimation_graph_search(oe).path())
print("\n---------------------------------------------\n")
print("Camino G-Z:\n")
print("Búsqueda en anchura:")
print(search.breadth_first_graph_search(gz).path())
print("\nBúsqueda en profundidad:")
print(search.depth_first_graph_search(gz).path())
print("\nBranch and Bound:")
print(search.branch_and_bound_graph_search(gz).path())
print("\nBranch and Bound con subestimación:")
print(search.branch_and_bound_with_subestimation_graph_search(gz).path())
print("\n---------------------------------------------\n")
print("Camino N-D:\n")
print("Búsqueda en anchura:")
print(search.breadth_first_graph_search(nd).path())
print("\nBúsqueda en profundidad:")
print(search.depth_first_graph_search(nd).path())
print("\nBranch and Bound:")
print(search.branch_and_bound_graph_search(nd).path())
print("\nBranch and Bound con subestimación:")
print(search.branch_and_bound_with_subestimation_graph_search(nd).path())
print("\n---------------------------------------------\n")
print("Camino M-F:\n")
print("Búsqueda en anchura:")
print(search.breadth_first_graph_search(mf).path())
print("\nBúsqueda en profundidad:")
print(search.depth_first_graph_search(mf).path())
print("\nBranch and Bound:")
print(search.branch_and_bound_graph_search(mf).path())
print("\nBranch and Bound con subestimación:")
print(search.branch_and_bound_with_subestimation_graph_search(mf).path())


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
