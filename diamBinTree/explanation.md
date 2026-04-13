## Diameter of Binary Tree #543

### Description:

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

### Algorithm:

For this problem, we use a global variable to track the diameter across all function calls.

For each node, we want to compute its height. To do this, we recursively find the height of its left and right subtrees and return the greater of the two values. If we reach a null node, we return 0, since the height of an empty subtree is 0.

Once we have the left and right subtree heights, we compute the height of the current node as:

`max(left, right) + 1`

We add 1 because the subtree heights do not include the current node itself.

At each node, we also check if the sum of the left and right heights forms a larger diameter than what we have seen so far. If it does, we update our global diameter.

This process continues until all nodes have been visited and we return the final diameter.

### Time Complexity:

The time complexity is O(n) because we visit each node exactly once during the DFS traversal.

### Space Complexity:

The space complexity is O(h), where h is the height of the tree, due to the recursive call stack. In the worst case (a skewed tree), this becomes O(n).

### Example of How the Algorithm Runs:

![CamScanner 4-11-26 21 28n](https://github.com/user-attachments/assets/aa1492bd-1e57-4952-aa42-71d5a8f60831)
