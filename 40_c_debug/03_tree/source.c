#include <stdio.h>
#include "tree.h"

// 叶子函数定义
void b1() {
    printf("Leaf Function 1\n");
}

void b2() {
    printf("Leaf Function 2\n");
}

void b_3() {
    printf("Leaf Function 3\n");
}

// 分支函数定义
void a1() {
    printf("Branch Function 1\n");
    b1();
    b2();
}

void a2() {
    printf("Branch Function 2\n");
    leafFunction3();
}

// 根函数定义
void rootFunction() {
    printf("Root Function\n");
    a1();
    a2();
}

// 主函数
int main() {
    rootFunction();
    return 0;
}
