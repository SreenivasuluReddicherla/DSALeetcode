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
    private HashMap<Integer, Integer> map;
    private int postorder_index;
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        map = new HashMap<>();
        postorder_index = postorder.length-1;
        for(int i=0;i<inorder.length;i++){
            map.put(inorder[i],i);
        }
        return arrayToTree(postorder, 0, inorder.length-1);
    }
    private TreeNode arrayToTree(int[] postorder, int left, int right){
        if(left>right){
            return null;
        }
        int root_val = postorder[postorder_index--];
        TreeNode root = new TreeNode(root_val);

        root.right = arrayToTree(postorder, map.get(root_val)+1, right);
        root.left = arrayToTree(postorder, left, map.get(root_val)-1);

        return root;
    }
}