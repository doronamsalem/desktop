#include <stdio.h>
#include <stddef.h>
int main()
{
 char *datatype[] = {"int", "string"};
 printf("size of %s is: %ld\n", datatype[0], sizeof(datatype[0]) );

}
