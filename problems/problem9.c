#include<stdio.h>
int main() {
    int n =10;
    int *p = &n;
    int newValue;
    printf("Original value: 10\n");
    printf("Enter new value: ");
    scanf("%d", &newValue);
    *p = newValue;
    printf("New value: %d", n);
    return 0;
}