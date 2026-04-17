## Max Area of Island #695

### Description:

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

### Algorithm:

This problem requires us to iterate over the grid and at each 1 we come across, if we haven't seen it yet, we perform a DFS and keep track of the current area of the island. After doing this while looping over the entire grid, we return the max of these found areas.

### Time Complexity:

O(m × n) because we iterate over the entire grid which is m × n in size.

### Space Complexity:

O(m × n) for the visited set or recursion stack in the worst case. If modifying the grid in place (marking visited cells), then O(min(m, n)) for the recursion stack depth.

### Example of How Algorithm Runs:

*(Add your diagram/example here if available)*
