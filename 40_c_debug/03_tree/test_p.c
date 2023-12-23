#include <stdio.h>
#include "tree.h"

// 函数接受指针参数
void modifyPointer(int *p) {
    my_dbg("addr p = %p\n", p);
    my_dbg("addr &p = %p\n", &p);
    *p = 42; // 修改指针指向的值
}

// 函数接受二级指针参数
void modifyDoublePointer(int **pp) {
    my_dbg("addr pp = %p\n", pp);
    my_dbg("addr *pp = %p\n", *pp);
    **pp = 52; // 修改二级指针指向的值
}

int main() {
    int x = 10;
    int *px = &x;

    my_dbg("addr x = %p\n", &x);
    my_dbg("add px = %p\n", px);

    printf("Before calling modifyPointer: x = %d\n", x);

    // 调用函数，传递指针参数
    modifyPointer(px);

    printf("After calling modifyPointer: x = %d\n", x);

    printf("Before calling modifyDoublePointer: x = %d\n", x);

    // 调用函数，传递二级指针参数
    modifyDoublePointer(&px);

    printf("After calling modifyDoublePointer: x = %d\n", x);

    return 0;
}
