## Binary Tree Right Side View #199

### Description:

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

### Algorithm:

In this problem we need to use a BFS to get the nodes on each level. Once all the nodes on each level are collected, we want to add to our answer array the rightmost node. We begin by declaring a queue with the root. We then perform a while loop while the queue is not empty. We get the length of the current level, and then add the rightmost node of this level to our answer array. We then loop over the entire level and collect the children. This process repeats until all nodes are searched.

### Time Complexity:

O(n) because we search the entire tree.

### Space Complexity:

O(w) where w is the maximum width of the tree (the maximum number of nodes at any level).

### Examples of How the Algorithm Runs:

![CamScanner 4-12-26 03 45n](https://github.com/user-attachments/assets/1ced0271-4ca6-44f7-9a82-1d85d17058fa)
