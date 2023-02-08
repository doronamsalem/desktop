#include <stdio.h>
#include <stdlib.h>


size_t JosephusProb (int n);

int main()
{
 int n = 0;
 printf( "please enter number of soldiers: ");
 scanf("%d", &n);
 printf("the index of thr last survivor from %d soliders is: %ld\n", n , JosephusProb (n) );
 return (0);
}





size_t JosephusProb (int n)
{
   int *arr = (int *)calloc(n , sizeof(int));
   size_t sword=0, next = sword + 1;

      while ( sword != next )
      {
          while ( arr[sword] == 1 )              /* while sword is dead */
          {
 	         sword = (sword+1) % n;
                 next = (sword+1) % n;
          }
    	  while (  arr[next] == 1 )   /* while next dead */
          {
                 next = (next+1) % n;
          }
          if ( sword != next )
	  {
       		 arr[next] = 1;           /* kill next */
          	sword = (next+1) % n;
          	next = (sword+1) % n;
      	  }
	}
      return sword;

}








