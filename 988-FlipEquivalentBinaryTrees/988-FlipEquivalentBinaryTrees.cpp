// Last updated: 7/21/2026, 7:08:59 PM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        // Base case: both nodes are null, so they are equivalent
        if (!root1 && !root2) return true;

        // If only one node is null or values don't match, return false
        if (!root1 || !root2 || root1->val != root2->val) return false;

        // Check both possible configurations: without flip and with flip
        bool noFlip = flipEquiv(root1->left, root2->left) &&
                      flipEquiv(root1->right, root2->right);

        bool flip = flipEquiv(root1->left, root2->right) &&
                    flipEquiv(root1->right, root2->left);

        // Return true if either configuration matches
        return noFlip || flip;
    }
};
