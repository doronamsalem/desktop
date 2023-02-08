#include <stdio.h>
#include "ex3_hello_hex.c"
#include "ex4_pow.c"
#include "ex5_flipnum.c"
#include "ex6_swap_value.c"
int main()
{
 /*exe 3:*/
 HelloHex();

 /*exe 4:*/
 int tester = 0; //test -3, 0 ,1 ,3
 printf("enter number for calculate 10^num: ");
 scanf("%d", &tester);
 printf("mypow result for %d is: %f\n", tester, mypow(tester) );

 /*exe 5:*/
 tester = 0; /*test 2, 12340*/
 printf("\nenter number and I will flip it: ");
 scanf("%d", &tester);
 printf("the fliped number for %d is: %1.2d\n", tester, flipNum(tester) );

 /*exe 6:*/
 int a = 1, b = 4;
 printf("\nthe value of a is: %d, the value of b is: %d\n", a, b);
 swapValue(&a, &b);
 printf("AFTER swaping the value of a is:%d, the value of b is:%d\n", a, b);
}
