## Max Difference Between Node and Ancestor #1026

### Description:

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

### Algorithm:

This problem requires a DFS because we need to recursively find the max and min node of each subtree. We run a DFS starting from the root. The base case is checking if the node == None, and if this is true, we have reached the end of a subtree. At this point we *should* have found our max and min nodes, and at this case we can return abs(currMax - currMin).

Otherwise, we need to update our currentMax and currentMin depending on the current node value. After this is done, we check the current node's left and right subtree. This process continues until both subtrees are checked.

Once both subtrees are checked, one of them will have a greater Max Difference Between a Node and Ancestor, so we return the max of left and right.

We call our DFS function by: `dfs(node.left or node.right, currmax, currmin)`. We include currmax and currmin because we need to track the max and min nodes along the entire subtree, and we do this by passing these values as params to pass them between function calls.

### Time Complexity:

The time complexity of this algorithm is O(n) because we traverse the tree once.

### Space Complexity:

The space complexity is O(h) where h is the height of the tree, because of the recursive call stack. In the worst case (skewed tree), this is O(n).

### Examples of How the Algorithm Runs:

![CamScanner 4-11-26 20 39n](https://github.com/user-attachments/assets/100e99bf-9fb9-415c-a488-68c0d6532cf0)
