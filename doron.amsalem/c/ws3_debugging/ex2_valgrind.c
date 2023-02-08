#include <stdlib.h>  /* malloc() */
#include <stdio.h>   /* printf() */
int main ()
{
  int *ptrint;
  ptrint = (int *)malloc(300);
  if (ptrint != NULL)
  {
     printf("great!");
  }
  else
  {
     printf("not great!");
  }
  free(ptrint);
  ptrint = NULL;
 return(0);
}
