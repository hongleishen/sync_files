#include <stdio.h>
#include "tree.h"

// tree_node *root;
// tree_node *current;


void _f_start_hook(const char *func)
{

}
#define f_start_hook()   _f_start_hook((const char *)__func__);

// 删除当前节点，current上移变parent
void _f_end_hook(const char *func)
{
    tree_node *tmp = current;
    printf("%s: run func is : %s, rm current node %s\n", __func__, func, current->data);

    remove_child(current->parent, current);
    current = tmp->parent;

    printf("current->data:%s, current->depth = %d;    set current->date:%s\n\n", tmp->data, tmp->depth, current->data);

}

#define f_end_hook() _f_end_hook((const char *)__func__);


// 叶子函数定义
void b1() {
    printf("%s\n", __func__);

    tree_node *b1 = create_node("b1");
    add_child(b1);

    f_end_hook();
}

void b2() {
    printf("%s\n", __func__);

    tree_node *b2 = create_node("b2");
    add_child(b2);

    f_end_hook();
}

// 分支函数定义
void a1() {
    printf("%s\n", __func__);

    tree_node *a1 = create_node("a1");
    add_child(a1);

    b1();
    b2();

    f_end_hook();
}

// ----------------------------------------
void b_3() {
    printf("%s\n", __func__);

    tree_node *b_3 = create_node("b_3");
    add_child(b_3);

    f_end_hook();
}

void a2() {
    printf("%s\n", __func__);

    tree_node *a2 = create_node("a2");
    add_child(a2);

    b_3();

    f_end_hook();
}

// --------------------------------------------
// 根函数定义
void rootFunction() {
    printf("%s\n", __func__);

    root = create_node("root");
    current = root;
    
    a1();
    a2();

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
