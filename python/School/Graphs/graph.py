"""
Project: Weighted Graphs
Author: Chris Walters
Course: CS 2420
Date: 4/29/2021

Description: Weighted graphs show up as a way to represent information in many applications, such as communication networks, water, power and energy systems, mazes, games and any problem where there is a measurable relationship between two or more things. It is therefore important to know how to represent graphs, and to understand important operations and algorithms associated with graphs. For this project, you will implement a directed, weighted graph and associated operations along with breadth-first search and Dijkstra's Shortest Path algorithms.

For this project, you will write a Graph ADT and a small main function as a small test driver “application”. Include main() in your graph.py source file with conditional execution.  It is common for modules to include a runnable main() to use for testing purposes.  It happens in this case, you will have both main() AND the test code we give you to test your implementation.
"""

from inspect import currentframe
import math


class Vertex:
    """
    Helper class for Graph
    Represents a vertex in the graph

    Attributes:
        label(str): a label which represents the vertex
        edges(list[Edge]): a list of Edges that have this vertex as the starting point
    """

    def __init__(self, label: str):
        """
        label(str): a label to represent the vertex
        """
        self.label = label
        self.edges = []
        self.paths = None

    def sort_edges(self):
        self.edges.sort(key=lambda x: x.weight)

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.label


class Edge:
    """
    Helper class for Graph
    represents a directed edge from one vertex to another

    Attributes:
        start(Vertex): the starting vertex
        end(Vertex): the ending vertex
        weight(float): the weight of the edge from start to end
    """

    def __init__(self, start, end, weight):
        """
        start(Vertex): the starting vertex
        end(Vertex): the ending vertex
        weight(float): the weight of the edge from start to end
        """
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return f'{self.start.label} -> {self.end.label}[label="{self.weight:.1f}",weight="{self.weight:.1f}"];'

    def __repr__(self):
        return f"{self.start.label} -> {self.end.label}: {self.weight:.1f}"


class Graph:
    """
    Represents a weighted directed graph,
        comprised of vertices and edges

    Attributes:
        vertices(list[Vertex]): the vertices present in the graph
    """

    def __init__(self):
        self.vertices = []

    def get_vert(self, label: str):
        """
        search vertices for a vertex
        """
        for i in self.vertices:
            if i.label == label:
                return i
        raise ValueError(f"vertex {label} could not be found")

    def add_vertex(self, label: str):
        """
        add a vertex with the specified label
        Return the graph
        label must be a string or raise ValueError
        """
        if not isinstance(label, str):
            raise ValueError(f"label {label} is not a string")
        # Check to see if the vertex already exists in the tree
        try:
            exists_vert = self.get_vert("label")
            raise ValueError(f"vertex {label} already in tree")
        except (ValueError):
            new_vertex = Vertex(label)
        self.vertices.append(new_vertex)
        return self

    def add_edge(self, src: str, dest: str, w):
        """
        add an edge from vertex src to vertex dest with weight w
        Return the graph
        validate src, dest, and w:
            raise ValueError if not valid
        """
        if not isinstance(w, (int, float)):
            raise ValueError(f"weight {w} is not a number")
        v_src, v_dest = self.get_vert(src), self.get_vert(dest)
        new_edge = Edge(v_src, v_dest, w)
        v_src.edges.append(new_edge)
        v_src.sort_edges()
        return self

    def get_weight(self, src: str, dest: str):
        """
        Return the weight (float) on edge src-dest
            (math.inf if no path exists,
            raise ValueError if src
            or dest not added to graph)
        """
        v_src, v_dest = self.get_vert(src), self.get_vert(dest)
        for i in v_src.edges:
            if i.end == v_dest:
                return i.weight
        return math.inf

    def dfs(self, starting_vertex: str):
        """
        Return a generator for traversing the graph in depth-first order starting from the specified vertex
        Raise a ValueError if the vertex does not exist
        """
        dfs_list = [self.get_vert(starting_vertex)]

        def recursive_dfs(vert):
            for i in vert.edges:
                if i.end not in dfs_list:
                    dfs_list.append(i.end)
                    recursive_dfs(i.end)

        recursive_dfs(self.get_vert(starting_vertex))
        return dfs_list

    def bfs(self, starting_vertex: str):
        """
        Return a generator for traversing the graph in breadth-first order starting from the specified vertex
        Raise a ValueError if the vertex does not exist
        """
        bfs_list = [self.get_vert(starting_vertex)]
        process_queue = [self.get_vert(starting_vertex)]
        while len(process_queue) > 0:
            current_item = process_queue.pop(0)
            for i in current_item.edges:
                if i.end not in bfs_list:
                    bfs_list.append(i.end)
                    process_queue.append(i.end)
        return bfs_list

    def dsp_table(self, src: str):
        source_vert = self.get_vert(src)
        if source_vert.paths is None:
            unvisited = [x.label for x in self.vertices]
            visited = []
            table = {}
            for i in unvisited:
                table[i] = [math.inf, ""]
            table[src][0] = 0

            while len(unvisited) > 0:
                current_item = self.get_vert(
                    sorted(
                        filter(lambda x: x[0] not in visited, table.items()),
                        key=lambda x: x[1][0],
                    )[0][0]
                )
                # Edges from the current item to vertices that haven't yet been visited
                unvisited_neighbors = [
                    neb
                    for neb in filter(
                        lambda edg: edg.end not in visited, current_item.edges
                    )
                ]
                # Distance from the source to the current item
                current_distance = table[current_item.label][0]
                for i in unvisited_neighbors:
                    # Distance from source to the target neighbor
                    src_distance = current_distance + i.weight
                    for j in table:
                        if i.end.label == j:
                            if src_distance < table[j][0]:
                                # Update the speed and previous vert for neighbor
                                table[j] = [src_distance, i.start.label]
                            break

                visited.append(current_item.label)
                unvisited.remove(current_item.label)

            source_vert.paths = table

    def dsp(self, src: str, dest: str):
        """
        Return a tuple (path length, the list of vertices on the path from destback to src)
        If no path exists, return the tuple (math.inf,  empty list)
        """
        self.dsp_table(src)
        source_point = self.get_vert(src)
        path_list = [dest]
        entry = source_point.paths[dest]
        length = entry[0]
        if length == math.inf:
            return (math.inf, [])
        backtrack = entry[1]
        while backtrack != "":
            path_list.append(backtrack)
            backtrack = source_point.paths[backtrack][1]

        path_list.reverse()
        return (length, path_list)

    def dsp_all(self, src):
        """
        Return a dictionary of the shortest weighted path between src and all other vertices using Dijkstra's Shortest Path algorithm
        In the dictionary, the key is the the destination vertex label, the value is a list of vertices on the path from src to dest inclusive
        """
        self.dsp_table(src)
        source_point = self.get_vert(src)
        basic_dict = {}
        for i in source_point.paths:
            if i != src:
                basic_dict[i] = self.dsp(src, i)[1]
        return basic_dict

    def __str__(self):
        """
        Produce a string representation of the graph that can be used with print()
        The format of the graph should be in GraphViz dot notation
        """
        string = "digraph G {\n"
        for i in self.vertices:
            for j in i.edges:
                string += f"   {str(j)}\n"
        string += "}"
        return string


def main():
    """
    1. Construct the graph shown in Figure 1 using your ADT
    2. Print it to the console in GraphViz notation as shown in Figure 1
    3. Print results of DFS starting with vertex “A” as shown in Figure 2
    4. BFS starting with vertex “A” as shown in Figure 3
    5. Print the path from vertex “ A” to vertex “F” (not shown here) using Djikstra’s shortest path algorithm (DSP) as a string like #3 and #4
    6. Print the shortest paths from “A” to each other vertex, one path per line using DSP
    """
    G = Graph()
    G.add_vertex("A")
    G.add_vertex("B")
    G.add_vertex("C")
    G.add_vertex("D")
    G.add_vertex("E")
    G.add_edge("A", "B", 6)
    G.add_edge("A", "D", 1)
    G.add_edge("D", "E", 1)
    G.add_edge("D", "B", 2)
    G.add_edge("E", "C", 5)
    G.add_edge("E", "B", 2)
    G.add_edge("B", "C", 5)
    print(G.dsp_all("A"))


if __name__ == "__main__":
    main()
