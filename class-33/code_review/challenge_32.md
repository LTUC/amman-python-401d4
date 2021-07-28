# Hashmap Tree Intersection

## Solution 1
- Preorder traverse the first tree, output will be A1 => O(n)
- Preorder traverse the second tree, output will be A2 => O(n)
- Loop over the first array and compare each item with each item in the second array using a nested loop O(n^2)
- Add the common itmes to the output array

Time Complexity:
O(n^2)

## Refactoring Solution 1
- Preorder traverse the first tree, output will be A1 => O(n)  [4,3,8,9,2]
- Preorder traverse the second tree, output will be A2 => O(n)  [9,5,4,2,76,5]
- New hashtable with values of A2 O(n) {9,5,4,2,76,5}
- Loop over the first array items and check if item in the hashtable => O(n)
- Add the common itmes to the output array

Time Complexity:
O(n)

