#include<stdio.h>
int main() {
    int x,y;
    printf("Input: \n");
    printf("Enter the first integer: ");
    scanf("%d", &x);
    printf("Enter the second integer: ");
    scanf("%d", &y);
    printf("Output: \n");
    if(x > y) {
        printf("The first integer is larger."); 
    } else if (y > x) {
        printf("The second integer is larger.");
    } else {
        printf("The two integers are equal.");
    }
    return 0;
}