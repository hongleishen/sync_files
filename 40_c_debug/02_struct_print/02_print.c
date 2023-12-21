#include <stdio.h>
#include <string.h>

typedef struct {
    char name[50];
    int age;
    float grade;
    char studentID[10];
} Student;

void print_type(void *var, const char *var_name, const char *type) {
    if (strcmp(type, "int") == 0) {
        printf("%s is an int with value: %d\n", var_name, *(int*)var);
    } else if (strcmp(type, "float") == 0) {
        printf("%s is a float with value: %f\n", var_name, *(float*)var);
    } else if (strcmp(type, "char[]") == 0) {
        printf("%s is a string with value: %s\n", var_name, (char*)var);
    } else {
        printf("%s is of an unknown type\n", var_name);
    }
}

#define PRINT_TYPE(x) print_type((void*)&(x), #x, \
                        __builtin_types_compatible_p(typeof(x), int) ? "int" : \
                        __builtin_types_compatible_p(typeof(x), float) ? "float" : \
                        __builtin_types_compatible_p(typeof(x), char[]) ? "char[]" : "unknown")

int main() {
    Student s = {"Alice", 20, 3.5, "S123"};

    // 打印结构体成员的类型和值
    PRINT_TYPE(s.name);
    PRINT_TYPE(s.age);
    PRINT_TYPE(s.grade);
    PRINT_TYPE(s.studentID);

    return 0;
}