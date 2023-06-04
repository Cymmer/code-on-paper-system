#include<stdio.h>
int main() {
    int n;
    float f;
    double d;
    char c;
    printf("Enter integer value: ");
    scanf("%d", &n);
    printf("Enter floating-point value: ");
    scanf("%f", &f);
    printf("Enter double-precision value: ");
    scanf("%lf", &d);
    printf("Enter a character: ");
    scanf(" %c", &c);
    printf("Gathered Inputs: \n");
    printf("int: %d\n", n);
    printf("float: %.2f\n", f);
    printf("double: %.2lf\n", d);
    printf("char: %c\n", c);
    return 0;
}