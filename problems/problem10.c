#include<stdio.h>

char getCharacter() {
    char c;
    scanf("%c", &c);
    return c;
}
void printMessage(char c) {
    printf("Welcome, %c!\n", c);
}
int decrement(int n) { return n-1; }
float half(float f) { return f/2; }
double fourth(double d) { return d/4; }
int main() {
    char c;
    int n;
    float f;
    double d;
    printf("Enter the first char of your name: ");
    c = getCharacter();
    printf("Enter an integer: ");
    scanf("%d", &n);
    printf("Enter a float: ");
    scanf("%f", &f);
    printf("Enter a double: ");
    scanf("%lf", &d);
    printMessage(c);
    printf("Decremented int is: %d\n", decrement(n));
    printf("Halved float is: %.2f\n", half(f));
    printf("Fourth of double is: %.2lf\n", fourth(d));
    return 0;
}
