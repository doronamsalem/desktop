#include <stdlib.h>  /*include malloc */
int *CopyArray ( int *current, int num_of_elements)  /* copy an int array and returnd the copy */
{
 int i, *copy;
 copy =(int *)malloc(sizeof(*current) * num_of_elements);

 if (copy == NULL)
  {
    printf("allocating memory didnt worked");
  }
 else
  {
    for ( i=0; i < num_of_elements; ++i )
    {
      *(copy + i) = *(current + i);
    }
  }
return copy;
}
