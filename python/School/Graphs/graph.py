"""
Project: Weighted Graphs
Author: Chris Walters
Course: CS 2420
Date: 4/29/2021

Description: Weighted graphs show up as a way to represent information in many applications, such as communication networks, water, power and energy systems, mazes, games and any problem where there is a measurable relationship between two or more things. It is therefore important to know how to represent graphs, and to understand important operations and algorithms associated with graphs. For this project, you will implement a directed, weighted graph and associated operations along with breadth-first search and Dijkstra's Shortest Path algorithms.

For this project, you will write a Graph ADT and a small main function as a small test driver “application”. Include main() in your graph.py source file with conditional execution.  It is common for modules to include a runnable main() to use for testing purposes.  It happens in this case, you will have both main() AND the test code we give you to test your implementation.
"""

import math


class Vertex:
    """
    Helper class for Graph
    Represents a vertex in the graph

    Attributes:
        label(str): a label which represents the vertex
        edges(list[Edge]): a list of Edges that have this vertex as the starting point
    """

    def __init__(self, label):
        """
        label(str): a label to represent the vertex
        """
        self.label = label
        self.edges = []
        return self

    def __str__(self):
        return self.label

    def __repr__(self):
        edges_string = ""
        for i in self.edges:
            edges_string += f"{i.end.label}, "
        edges_string = edges_string[:-2]
        return f"{self.label} with edges to {edges_string}"


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
        return self

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
        return self

    def add_vertex(self, label):
        """
        add a vertex with the specified label
        Return the graph
        label must be a string or raise ValueError
        """
        if not isinstance(label, str):
            raise ValueError(f"label {label} is not a string")
        new_vertex = Vertex(label)
        self.vertices.append(new_vertex)
        return self

    def check_for_vert(self, label):
        """
        search vertices for a vertex
        """
        for i in self.vertices:
            if i.label == label:
                return i
        raise ValueError(f"vertex {label} could not be found")

    def add_edge(self, src, dest, w):
        """
        add an edge from vertex src to vertex dest with weight w
        Return the graph
        validate src, dest, and w:
            raise ValueError if not valid
        """
        if not isinstance(w, (int, float)):
            raise ValueError(f"weight {w} is not a number")
        v_src, v_dest = self.check_for_vert(src), self.check_for_vert(dest)
        new_edge = Edge(v_src, v_dest, w)
        v_src.edges.append(new_edge)
        return self

    def get_weight(self, src, dest):
        """
        Return the weight (float) on edge src-dest
            (math.inf if no path exists,
            raise ValueError if src
            or dest not added to graph)
        """
        v_src, v_dest = self.check_for_vert(src), self.check_for_vert(dest)
        for i in v_src.edges:
            if i.end == v_dest:
                return i.weight
        return math.inf

    def dfs(self, starting_vertex):
        """
        Return a generator for traversing the graph in depth-first order starting from the specified vertex
        Raise a ValueError if the vertex does not exist
        """
        pass

    def bfs(self, starting_vertex):
        """
        Return a generator for traversing the graph in breadth-first order starting from the specified vertex
        Raise a ValueError if the vertex does not exist
        """
        pass

    def dsp(self, src, dest):
        """
        Return a tuple (path length, the list of vertices on the path from destback to src)
        If no path exists, return the tuple (math.inf,  empty list)
        """
        pass

    def dsp_all(self, src):
        """
        Return a dictionary of the shortest weighted path between src and all other vertices using Dijkstra's Shortest Path algorithm
        In the dictionary, the key is the the destination vertex label, the value is a list of vertices on the path from src to dest inclusive
        """
        pass

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
    pass


if __name__ == "__main__":
    main()
