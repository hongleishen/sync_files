#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tree.h"

/*
// 定义树节点结构体
typedef struct tree_node {
    char *data;
    struct tree_node* *children; // 子节点数组
    int child_count;            // 子节点数量
} tree_node;
*/

// 创建新节点
tree_node *create_node(const char *data) {
    tree_node *node = (tree_node*)malloc(sizeof(tree_node));
    node->data = strdup(data); // 复制字符串
    node->children = NULL;
    node->child_count = 0;
    return node;
}

// 添加子节点
void add_child(tree_node *parent, tree_node *child) {
    parent->child_count++;
    parent->children = (tree_node**)realloc(parent->children, sizeof(tree_node*)  *parent->child_count);
    parent->children[parent->child_count - 1] = child;
}

// 前序遍历
void preorder_traversal(tree_node *node) {
    if (node == NULL) return;
    printf("%s ", node->data);
    for (int i = 0; i < node->child_count; i++) {
        preorder_traversal(node->children[i]);
    }
}

// 后序遍历
void postorder_traversal(tree_node *node) {
    if (node == NULL) return;
    for (int i = 0; i < node->child_count; i++) {
        postorder_traversal(node->children[i]);
    }
    printf("%s ", node->data);
}

// 搜索节点
tree_node *search(tree_node *node, const char *data) {
    if (node == NULL) return NULL;
    if (strcmp(node->data, data) == 0) return node;
    for (int i = 0; i < node->child_count; i++) {
        tree_node *result = search(node->children[i], data);
        if (result != NULL) return result;
    }
    return NULL;
}

// 释放树内存
void free_tree(tree_node *node) {
    if (node == NULL) return;
    for (int i = 0; i < node->child_count; i++) {
        free_tree(node->children[i]);
    }
    free(node->data);
    free(node->children);
    free(node);
}


// 移除子节点
void remove_child(tree_node *parent, tree_node *child) {
    if (parent == NULL || child == NULL) return;

    // 创建一个新的子节点数组
    int new_count = 0;
    tree_node* *new_children = malloc(sizeof(tree_node*)  *parent->child_count);
    
    // 复制除了要移除的子节点外的所有子节点
    for (int i = 0; i < parent->child_count; i++) {
        if (parent->children[i] != child) {
            new_children[new_count++] = parent->children[i];
        }
    }

    // 释放原来的子节点数组
    free(parent->children);

    // 更新父节点的子节点数组和计数
    parent->children = new_children;
    parent->child_count = new_count;
}

#if 0
int main() {
    / * 创建树
                         root
                child1           child2

            child3                    child4
    */
    tree_node *root = create_node("Root");
    tree_node *child1 = create_node("Child1");
    tree_node *child2 = create_node("Child2");
    tree_node *child3 = create_node("Child3");
    tree_node *child4 = create_node("Child4");

    add_child(root, child1);
    add_child(root, child2);
    add_child(child1, child3);
    add_child(child2, child4);

    // 遍历树
    printf("Preorder Traversal:\n");
    preorder_traversal(root);

    printf("\n\nPostorder Traversal:\n");
    postorder_traversal(root);
    printf("\n");

    // 搜索节点
    tree_node *search_result = search(root, "Child3");
    if (search_result) {
        printf("\nNode found: %s\n", search_result->data);
    } else {
        printf("\nNode not found\n");
    }

    // 释放树内存
    // free_tree(root);
    printf("\n");
    remove_child(root, child2);
    preorder_traversal(root);
    printf("\n");

    return 0;
}
#endif

/*
topeet@ubuntu:~/wks/06_sync_files/40_c_debug/03_tree$ ./a.out
Preorder Traversal:
Root Child1 Child3 Child2 Child4

Postorder Traversal:
Child3 Child1 Child4 Child2 Root

Node found: Child3

Root Child1 Child3
*/