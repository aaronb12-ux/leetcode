# Reachable Nodes With Restrictions

## Description:
There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.

## Algorithm:
This problem requires a BFS because we need to check nodes level by level. We check level by level because we are not 'searching' for anything we are seeing how many total nodes aren't restricted. At each level we can see if any of the nodes are restricted, if they are, then we won't continue down that path in the search. If a node is not restricted, then we increment our answer and add that node to the queue to search its unseen neighbors down the line.

## Time Complexity:
O(N) where N is the number of nodes in the tree

## Space Complexity:
O(N) because we store all nodes in a hashmap as keys
