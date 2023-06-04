#include<stdio.h>
int main() {
    char name[100]; int age;
    printf("Enter your name: ");
    scanf("%[^\n]s", name);
    printf("Enter your age: ");
    scanf("%d", &age);
    printf("Your name is %s and you are %d years old.", name, age);
    return 0;
}