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
    private HashMap<Integer, Integer> inordermap;
    private int preorderindex;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inordermap  = new HashMap<>();
        preorderindex = 0;
        for(int i=0;i<inorder.length;i++){
            inordermap.put(inorder[i],i);
        }
        return arrayToTree(preorder, 0, inorder.length-1);
    }
    private TreeNode arrayToTree(int[] preorder, int left, int right){
        if(left>right){
            return null;
        }
        int root_val = preorder[preorderindex++];
        TreeNode root = new TreeNode(root_val);
        root.left = arrayToTree(preorder, left, inordermap.get(root_val)-1);
        root.right = arrayToTree(preorder, inordermap.get(root_val)+1, right);
        return root; 
    }
}