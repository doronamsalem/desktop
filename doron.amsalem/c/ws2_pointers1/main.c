#include <stdio.h>        /*include all basic funcs(printf, scanf..) */
#include <assert.h>              /*execise 1 of string*/
#include "ex1_SwapInts.c"        /* include SwapInts()  */
#include "ex2_CopyArr.c"         /* include CopyArray() */
#include "ex4_two_size.c"        /* include SwapSize_tVars */
#include "ex4_two_pointers.c"    /* include SwapSize_tpointers */
#include "ex_string.c"           /* incluse StrLen() StrCmp() */

#ifndef ARR_SIZE
  #define ARR_SIZE(array) (sizeof(array)/sizeof(array[0]))
#endif
#ifndef EXIT_SUCCESS
  #define EXIT_SUCCESS 0
#endif
int main()
{
 printf("\n*exercis 1:\n" );
 {
  int num1=3, num2=6;
  printf("Before swaping value of num1: %d and num2: %d\n", num1, num2);
  SwapInts(&num1, &num2);
  printf("After swaping value of num1: %d and num2: %d\n", num1, num2);
 }

 printf("\n*exercis 2:\n");
 {
  int arr[] = {1 ,2 ,3 ,4 ,5 ,6}, *copy;
  size_t i, elements = ARR_SIZE(arr);
  copy = CopyArray(arr, elements);
  printf("array elements:");
  for (i = 0; i < elements; i++)
  {
        printf("  %d", arr[i]);
  }
  printf("\n");
  printf("copied elements:");
  for (i = 0; i < elements; i++)
  {
        printf("  %d",*(copy + i));
  }
  free(copy);
  printf("\n");
}


 /* printf("*exercis 4 by value:\n");
 {
  size_t num1 = 7, num2 = 10;
  printf("Before SwapSize_tVars() value of num1: %ld and num2: $ld\n", num1, num2);
  num1, num2 = SwapSize_tVars(num1, num2);
  printf("After SwapSize_tVars() value of num1: %ld and num2: $ld\n", num1, num2);
 }
 */

 printf("\n*exercis 4 two size_t:");
 {
  size_t num1 = 4, num2 = 8;
  printf("\nBefore SwapSize_tRef() value of num1: %ld and num2: %ld\n", num1, num2);
  SwapSize_tRef(&num1, &num2);
  printf("After SwapSize_tREF() value of num1: %ld and num2: %ld\n", num1, num2);
 }

 printf("\n*exercise 1 of string:\n");
 {
  char exit, str1[11], str2[11];
  exit = 'n';
  while ( exit != 'y' && exit != 'Y' )
    {
      printf("enter two strings for str1, str2(max 10 chars)\npress enter after each string:\n");
      scanf("%s", str1);
      scanf("%s", str2);
      printf("\nsize of str1 is: %ld\n", StrLen(str1) );
      printf("size of str2 is: %ld\n", StrLen(str2) );
      printf("StrCmp result for str1 vs str2 is: %d\n", StrCmp(str1, str2) );
      printf("StrCmp result for str2 vs str1 is: %d\n", StrCmp(str2, str1) );
      printf("do you want to exit?[y/n] ");
      scanf(" %c", &exit);
      assert(exit == 'y' || exit == 'n');
    }
  }
   return EXIT_SUCCESS;
}


