#include "ex1.c"
#include "ex2.c"

int main()
{
 char str[] = {"HellOw WOrld"};
 int n = 0;
 printf("enter num for TF(): ");
 scanf("%d", &n);
 TF(n);

 Revere_Low(str);

 return (0);
}
