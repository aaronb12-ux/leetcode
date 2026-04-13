## Largest Value In Each Tree Row #515

### Description:

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

### Algorithm:

We implement a BFS to search the tree level by level, and add to our 'ans' variable the max node on each level. We begin by declaring a queue with the root. This is level 0. We then continue to search the tree while the queue is not empty. For each level, we iterate through the nodes and find the max node. For each node, we see if it's the current max and update our currMax variable, and add the current node's neighbors to the queue. After iterating through the level, we add the currentMax to our ans and reset the current max to -infinity.

### Time Complexity:

O(n) because our BFS traverses the entire tree.

### Space Complexity:

O(w) where w is the width of the tree (the maximum number of nodes at any level). The nodes are stored in the queue.

### Example of How Algorithm Runs:

![CamScanner 4-12-26 19 49n](https://github.com/user-attachments/assets/090fb3ec-9126-4f18-9ad5-f41b6537cca6)
