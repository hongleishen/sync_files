#ifndef TREE_H
#define TREE_H

// 定义树节点结构体
typedef struct TreeNode {
    char* data;
    struct TreeNode** children; // 子节点数组
    int child_count;            // 子节点数量
} TreeNode;


TreeNode* create_node(const char* data);
void add_child(TreeNode* parent, TreeNode* child);

void preorder_traversal(TreeNode* node);
void postorder_traversal(TreeNode* node);
TreeNode* search(TreeNode* node, const char* data);

void free_tree(TreeNode* node);
void remove_child(TreeNode* parent, TreeNode* child);

#endif