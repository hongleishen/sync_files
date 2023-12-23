#ifndef TREE_H
#define TREE_H

// 定义树节点结构体
typedef struct tree_node {
    char *data;
    struct tree_node **children; // 子节点数组
    int child_count;            // 子节点数量

    struct tree_node *parent;           // 父节点
    struct tree_node *current_parent;   // 当前节点
    int depth;                          // 节点深度
} tree_node;


tree_node *create_node(const char *data);
void add_child(tree_node *parent, tree_node *child);

void preorder_traversal(tree_node *node);
void postorder_traversal(tree_node *node);
tree_node *search(tree_node *node, const char *data);

void free_tree(tree_node *node);
void remove_child(tree_node *parent, tree_node *child);

#endif