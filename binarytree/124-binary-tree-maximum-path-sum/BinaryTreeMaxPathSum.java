/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int maxSum;
    public int maxPathSum(TreeNode root) {
        maxSum = Integer.MIN_VALUE;
        dfs(root);
        return maxSum;
    }
    private int dfs(TreeNode node){
        if(node == null){
            return 0;
        }
        int leftVal = Math.max(0, dfs(node.left));
        int rightVal = Math.max(0, dfs(node.right));
        int currentSum = node.val + leftVal + rightVal;
        maxSum = Math.max(maxSum, currentSum);
        
        return node.val + Math.max(leftVal, rightVal);

    }
}