#include <stdio.h>

void TF (int num)
{
  int i;
  for (i = 1; i <= num; i++)
  {
      if (i % 15 == 0)
      {
 	 printf("TF\n");
      }
      else  if (i % 5 == 0)
      {
         printf("F\n");
      }
      else if (i % 3 == 0)
      {
         printf("T\n");
      }
      else
      {
	printf("%d\n",i);
      }
  }
}
