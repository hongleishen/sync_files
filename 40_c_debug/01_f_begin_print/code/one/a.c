#include <stdio.h>


int add(int a, int b) 
{
    return a + b;
}


int factorial(int n) 
{
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}


bool isPrime(int n) 
{
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
