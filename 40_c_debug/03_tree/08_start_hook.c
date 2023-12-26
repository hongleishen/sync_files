#include <stdio.h>
#include "tree.h"

// tree_node *root;
// tree_node *current;

#define d_printf(format, ...)    do {    \
    for (int i = 0; i < 4*current->depth; i++) {    \
        printf(" ");    \
    }   \
    if (format[0] != '\0') \
        printf(format, ##__VA_ARGS__); \
} while(0);


static void _f_start_hook(const char *func)
{
    if (root == NULL) {
        my_dbg(" root == NULL, return\n");
        return;
    }

    tree_node *func_node = create_node(func);
    add_child(func_node);

    d_printf("%s\n", func);

    return;
}
#define f_start_hook()   _f_start_hook((const char *)__func__);

// 删除当前节点，current上移变parent
static void _f_end_hook(const char *func)
{
    if (root == NULL) {
        my_dbg(" root == NULL, return\n");
        return;
    }

    tree_node *tmp = current;

    d_printf("--");
    preorder_traversal(root);
    printf("\n");

    remove_child(current->parent, current);
    d_printf("current->data:%s, current->depth = %d;  set current to %s\n\n", tmp->data, tmp->depth, tmp->parent->data);
    current = tmp->parent;
    return;
}
#define f_end_hook() _f_end_hook((const char *)__func__);


// ---------------func b------------------------------
// 叶子函数定义
void b1() {
    f_start_hook();
    f_end_hook();
}

void b2() {
    f_start_hook();
    f_end_hook();
}

void b_3() {
    f_start_hook();
    f_end_hook();
}


// --------func a--------------------------------
// 分支函数定义
void a1() {
    f_start_hook();

    b1();
    b2();

    f_end_hook();
}


void a2() {
    f_start_hook();

    b_3();

    f_end_hook();
}

// -------------------func root-------------------------
// 根函数定义      必须跟函数初始化root后，后面的树形结构才会运行，在此之前，函数都直接跳过
void rootFunction() {
    f_start_hook();
    printf("%s\n", __func__);

    root = create_node("root");
    current = root;
    
    a1();
    a2();

    free_tree(&root);
    if (root == NULL) 
        my_dbg("root is null after free\n");
    else
        my_dbg("root is not null after free\n");


    f_end_hook();
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
    //preorder_traversal(root);
    printf("\n");


    return 0;
}

/*
[dbg: _f_start_hook, 19 ] root == NULL, return
rootFunction
    a1
        b1
        --root,0;    a1,1;    b1,2;
        current->data:b1, current->depth = 2;  set current to a1

        b2
        --root,0;    a1,1;    b2,2;
        current->data:b2, current->depth = 2;  set current to a1

    --root,0;    a1,1;
    current->data:a1, current->depth = 1;  set current to root

    a2
        b_3
        --root,0;    a2,1;    b_3,2;
        current->data:b_3, current->depth = 2;  set current to a2

    --root,0;    a2,1;
    current->data:a2, current->depth = 1;  set current to root

[dbg: free_tree, 143 ]node->data = root
[dbg: rootFunction, 106 ]root is null after free
[dbg: _f_end_hook, 36 ] root == NULL, return

-------preorder_traversal:
*/