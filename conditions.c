#include <stdio.h>

int main()
{
    int age;
    age = 13;

    // if (age == 20)
    // {
    //     printf("Left\n");
    // }
    // else if (age < 14)
    // {
    //     printf("next Kids\n");
    // }
    // else
    // {
    //     printf("Right\n");
    // }
    age = 20;
    switch (age)
    {
    case 20:
        printf("Left\n");
        break;
    case 15:
        printf("Kids\n");
        break;
    default:
        printf("Invalide\n");
    }
}