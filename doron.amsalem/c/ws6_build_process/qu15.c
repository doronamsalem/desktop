#include <stdlib.h>
void foo()
{
char str1[20];
char *str2 ;
char *str3 ="what";
char str4[] ="what";
}

void main ()
{
  foo();
  char *str3 ="what";
  str3[0] = 'a';
}
