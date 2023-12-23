#include <stdio.h>
#include "tree.h"

tree_node *root;
tree_node *current_parent;

// 叶子函数定义
void _b1() {
    printf("%s\n", __func__);

    tree_node *b1 = create_node("b1");
    add_child(current_parent, b1);
}

void _b2() {
    printf("%s\n", __func__);

    tree_node *b2 = create_node("b2");
    add_child(current_parent, b2);
}

// 分支函数定义
void _a1() {
    printf("%s\n", __func__);

    tree_node *a1 = create_node("a1");
    add_child(root, a1);
    current_parent = a1;

    _b1();
    _b2();
}

// ----------------------------------------
void _b_3() {
    printf("%s\n", __func__);

    tree_node *b_3 = create_node("b_3");
    add_child(current_parent, b_3);
}

void _a2() {
    printf("%s\n", __func__);

    tree_node *a2 = create_node("a2");
    add_child(root, a2);
    current_parent = a2;

    _b_3();
}

// --------------------------------------------
// 根函数定义
void rootFunction() {
    printf("%s\n", __func__);

    root = create_node("root");
    current_parent = root;
    
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
    rootFunction();

    printf("\n-------preorder_traversal:\n");
    preorder_traversal(root);
    printf("\n");
    return 0;
}
