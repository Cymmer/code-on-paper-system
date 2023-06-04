#include <stdio.h>
int main() {
    int n[10];
    int i;
    printf("Enter 10 integers: ");
    for(i = 0; i < 10; i++) {
        scanf("%d", &n[i]);
    }
    printf("Output: [");
    for(i = 0; i < 9; i++) {
        printf("%d,", n[i]);
    }
    printf("%d]", n[i]);
    return 0;
}
