#include<stdio.h>
int main() {
    int piggyBank = 0; int newValue;
    do {
        printf("Enter value: ");
        scanf("%d", &newValue);
        if(newValue >= 0) {
            piggyBank += newValue;
            printf("Piggy Bank: %d\n", piggyBank);
        }
    } while(newValue >= 0);
    printf("Piggy Bank Broken");
    return 0;
}