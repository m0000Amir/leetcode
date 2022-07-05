
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var checkTree = function(root) {
    if ((root.left.val + root.right.val) === root.val) return true
    return false  
};

const rootList = [5,3,1];
let treeNode = new TreeNode(val = rootList[0]);
treeNode.left = new TreeNode(val = rootList[1]);
treeNode.right = new TreeNode(val = rootList[2]);

console.log(checkTree(treeNode));
