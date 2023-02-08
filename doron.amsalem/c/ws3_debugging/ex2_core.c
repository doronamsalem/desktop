/*#include <stdlib.h>*/
#include <stdio.h>
int main()
{
/*int i = 0;
  while (1)
{
 ++i;
 printf("it cuold be great for school punishment  ");
 if (i == 100)
  {
    abort();
  }
}
}  */
int *ptr = 0, arr[]={0,1,2,3}, i = 0;
while(i < 100)
{
 if (arr[i] == 3)
   *ptr = arr[i];
else
   printf("%d\n", i);
++i;
}
return 0;
}
