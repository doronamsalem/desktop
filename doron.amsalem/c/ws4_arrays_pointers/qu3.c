#include <stdio.h>

int main()
{
    printf("short int:    %ld bytes\n", sizeof(short int));
    printf("unsigned short int:    %ld bytes\n", sizeof(unsigned short int));
    printf("int:          %ld bytes\n", sizeof(int));
    printf("long int:     %ld bytes\n", sizeof(long int));
    printf("char:         %ld bytes\n", sizeof(char));
    printf("unsigned char:         %ld bytes\n", sizeof(unsigned char));
    printf("float:        %ld bytes\n", sizeof(float));
    printf("double:       %ld bytes\n", sizeof(double));
    printf("long double: %ld bytes\n", sizeof(long double));
    printf("size_t:         %ld bytes\n", sizeof(size_t));

    return (0);
}
