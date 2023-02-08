/*exe1
a:
    void firstoption(intarr, int row, int column);
    void secondoption( int arr[][], int row, int column); 

b:
    firstoption:(arr+((icolumn)+j));
    secondoption: arr[row][column];

c:
    firstoption: sizeof(arr / arr[][]) = sizeof( pointer )      (function)
      secondoption: sizeof(arr[][]) = elements sizeof( arr[0][0] )    (main)

*/


#include <stdio.h>   /* printf(),scanf() */
#include <stdlib.h>  /* sizeof() */

int *SumRowes(int *matrix , int rows, int colum);

int main ()
{
        int *array = NULL, rows = 0, colums = 0, x = 0, i = 0;
        printf ("enter numbers of rows: ");
        scanf ("%d", &rows);
        printf ("enter numbers of colums: ");
        scanf ("%d", &colums);

         array = (int *)malloc(colums * rows * sizeof(int));   /* pointer for two dimensions array */
         if(array == NULL)
         {
                  printf ("initialization failed" );
         }
         else
         {
                  for (i = 0; i < rows; i++)
                 {
                         for(x = 0; x < colums; x++)
                         {
                                 printf ("enter number to row %d, colum %d: ", i+1 , x+1);
                                 scanf("%d",  array + (i * colums) + x  );           /* initialize elements array */
                         }
                 }
         }

      /*  InisializeTwoDim(array, rows, colums); */
        SumRowes( array, rows, colums);
        return (0);
}



int *SumRowes(int *matrix , int rows, int colum)  /* gets two dimensions array, return array with sum of each row */
{
	int *sums = NULL, i = 0, x = 0;
	sums = (int *)calloc(rows, sizeof(int) );     /* array for sum of each row */
	if ( sums == NULL )
 	{
    		printf("allocation failed");
	}
	else
	{
		for (i = 0; i < rows; i++ )
 		{
	    		for (x = 0; x < colum; x ++ )
    			{
				*(sums + i) +=  *(matrix + (i * colum) + x);   /* clculate sum of each row */
    			}
 		}

 		for ( i = 0; i < rows; i++ )
 		{
   			printf("sum of row %d is: %d\n",i , *(sums + i));    /* prints all sums */
 		}
	}
	return sums;
}
/*
void InisializeTwoDim(int *array, int rows, int colums)
{
        int x = 0, i = 0;

        array = (int *)malloc(colums * rows * sizeof(int));   /* pointer for two dimensions array */
/*        if(array == NULL)
	{
		printf ("initialization failed" );
	}
	else
	{
		 for (i = 0; i < rows; i++)
        	{
               		for(x = 0; x < colums; x++)
                	{
                       		printf ("enter number to row %d, colum %d: ", i+1 , x+1);
                       		scanf("%d",  array + (i * colums) + x  );           /* initialize elements array */
  /*              	}
        	}
	}
}
*/


