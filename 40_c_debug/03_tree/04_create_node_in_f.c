#include <stdio.h>
#include "tree.h"

tree_node *root;

// 叶子函数定义
void _b1(tree_node *parent) {
    tree_node *b1 = create_node("b1");
    printf("%s\n", __func__);
    add_child(parent, b1);
}

void _b2(tree_node *parent) {
    tree_node *b2 = create_node("b2");
    printf("%s\n", __func__);
    add_child(parent, b2);
}

// 分支函数定义
void _a1() {
    tree_node *a1 = create_node("a1");
    printf("%s\n", __func__);
    add_child(root, a1);
    _b1(a1);
    _b2(a1);
}

// ----------------------------------------
void _b_3(tree_node *parent) {
    tree_node *b_3 = create_node("b_3");
    printf("%s\n", __func__);
    add_child(parent, b_3);
}

void _a2() {
    tree_node *a2 = create_node("a2");
    printf("%s\n", __func__);
    add_child(root, a2);
    _b_3(a2);
}

// --------------------------------------------
// 根函数定义
void rootFunction() {
    printf("%s\n", __func__);
    _a1();
    _a2();
}

/*
               root
        a1              a2
    b1     b2            b_3
*/

// 主函数
int main() {
    root = create_node("root");
    rootFunction();
    preorder_traversal(root);
    printf("\n");
    return 0;
}
