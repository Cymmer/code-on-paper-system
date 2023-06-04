#include <stdio.h>
int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);
    int sum = 0;
    for(int i = 1; i <= n; i++) {
        sum += i;
    }
    printf("Output: The sum of the first %d natural numbers is %d", n, sum);
    return 0;
}