#include<stdio.h>
int main() {
    int n;
    printf("Enter input: ");
    scanf("%d", &n);
    switch(n) {
        case 1:
            printf("Output: ON");
            break;
        case 0:
            printf("Output: OFF");
            break;
        default:
            printf("Output: ERR");
            break;
    }
    return 0;
}