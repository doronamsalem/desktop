#include <stdio.h>
#include <stdlib.h>

int main()
{
int *ptr;
ptr = malloc(50);
if (*(ptr + 2) == 5) 
    {
        printf("success");
    }
else
    {
        printf("failed");
    }
 return (0);
}
