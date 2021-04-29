"""
Project: Weighted Graphs
Author: Chris Walters
Course: CS 2420
Date: 4/29/2021

Description: Weighted graphs show up as a way to represent information in many applications, such as communication networks, water, power and energy systems, mazes, games and any problem where there is a measurable relationship between two or more things. It is therefore important to know how to represent graphs, and to understand important operations and algorithms associated with graphs. For this project, you will implement a directed, weighted graph and associated operations along with breadth-first search and Dijkstra's Shortest Path algorithms.

For this project, you will write a Graph ADT and a small main function as a small test driver “application”. Include main() in your graph.py source file with conditional execution.  It is common for modules to include a runnable main() to use for testing purposes.  It happens in this case, you will have both main() AND the test code we give you to test your implementation.
"""


class Graph:
    """
    ADT representing a weighted directed graph, comprised of vertices and edges
    """

    def __init__(self):
        pass

    def add_vertex(self, label):
        """
        add a vertex with the specified label
        Return the graph
        label must be a string or raise ValueError
        """
        pass

    def add_edge(self, src, dest, w):
        """
        add an edge from vertex src to vertex dest with weight w
        Return the graph
        validate src, dest, and w:
            raise ValueError if not valid
        """
        pass

    def get_weight(self, src, dest):
        """
        Return the weight (float) on edge src-dest
            (math.inf if no path exists,
            raise ValueError if src
            or dest not added to graph)
        """
        pass

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
        pass


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
