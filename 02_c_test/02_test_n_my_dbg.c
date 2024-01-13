#include <stdio.h>
#define my_dbg(format, ...)   printf("[dbg: %s, %s, %d] " format, __FILE__, __func__, __LINE__, ##__VA_ARGS__)

// printf 一行
#define n_my_dbg(format, ...)                              \
    int n = 0;                                             \
    const char *new_format = format;                       \
    do {                                                   \
        while (*new_format == '\n') {                      \
            new_format++;                                  \
            n++;                                           \
        }                                                  \
        printf("number = %d\n", n);                        \
        char complete_format[256];                         \
        snprintf(complete_format, sizeof(complete_format), "[dbg: %s, %s, %d] %s", __FILE__, __func__, __LINE__, new_format); \
        printf(complete_format, ##__VA_ARGS__);            \
    } while (0)


// 2行
#define n_my_dbg2(format, ...)                              \
    int _n = 0;                                             \
    const char *new_format_ = format;                       \
    do {                                                   \
        while (*new_format_ == '\n') {                      \
            new_format_++;                                  \
            _n++;                                           \
        }                                                  \
        printf("number = %d\n", _n);                        \
        printf("[dbg: %s, %s, %d] ", __FILE__, __func__, __LINE__); \
        printf(new_format_, ##__VA_ARGS__);                 \
    } while (0)


// 正式 打印 \n 函数
#define n_my_dbg3(format, ...)              \
    char *new_format__ = format;      \
    do {                                    \
        while (*new_format__ == '\n') {     \
            new_format__++;                 \
            printf("\n");                   \
        }                                   \
        printf("[dbg: %s, %s, %d] ", __FILE__, __func__, __LINE__); \
        printf(new_format__, ##__VA_ARGS__);                 \
    } while (0)


#define n_my_dbg4(format, ...)                                  \
    do {                                                        \
        const char *new_format__ = format;                      \
            while (*new_format__ == '\n') {                     \
                new_format__++;                                 \
                printf("\n");                                   \
            }                                                   \
            printf("[dbg: %s, %s, %d] ", __FILE__, __func__, __LINE__); \
            printf(new_format__, ##__VA_ARGS__);                \
    } while (0)


void main(void)
{
    int i = 0;
    printf("start ^^^^^^^^^^^\n");
    my_dbg("i = %d\n", i++);
    my_dbg("\ni = %d\n", i++);
    n_my_dbg("\n\n\ni = %d\n", i++);
    n_my_dbg2("\n\n\ni = %d\n", i++);
    //n_my_dbg3("\n\n\ni = %d\n", i++);
    //n_my_dbg3("\n\n\ni = %d\n", i++);
    n_my_dbg4("\n\n\ni = %d\n", i++);
    n_my_dbg4("\n\n\ni = %d\n", i++);
    printf("end ==============\n");
}