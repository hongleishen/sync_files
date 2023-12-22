#include <stdio.h>


#define PrintValue(x) \
    do { \
        _Generic((x), \
            int:    printf("x is an integer: %d\n", x), \
            double: printf("x is a double: %lf\n", (double)x), \
            default: printf("x is of an unknown type\n") \
        ); \
    } while (0)



int main() {
    int a = 42;
    double b = 3.14;
    char c = 'A';

    PrintValue(a); // 输出：x is an integer: 42
    PrintValue(b); // 输出：x is a double: 3.140000
    PrintValue(c); // 输出：x is of an unknown type

    return 0;
}
