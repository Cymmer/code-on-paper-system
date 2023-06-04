#include<stdio.h>
int main() {
    int v1, v2;
    printf("Enter 1st value: ");
    scanf("%d", &v1);
    printf("Enter 2nd value: ");
    scanf("%d", &v2);
    int sum = v1 + v2;
    printf("Addition: %d", sum);
    int sub = v1 - v2;
    printf("Subtraction: %d", sub);
    int mul = v1 * v2;
    printf("Multiplication: %d", mul);
    float division = v1 / (float)v2;
    printf("Division: %.2f", division);
    int modulo = v1 % v2;
    printf("Modulo: %d", modulo);
    return 0;
}