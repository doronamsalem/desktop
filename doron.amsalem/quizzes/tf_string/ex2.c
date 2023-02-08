#include <stdio.h>
#include <ctype.h>
#include <string.h>

void Revere_Low (char *str)
{
  size_t len = 0, i = 0;
  char temp = '0';
  len = strlen(str) - 1;        /*last index*/

  printf("source string: %s\n", str);
  for (; i < len; i++, len--)
  {
    temp = tolower( *(str + i) );
    *(str + i) = tolower( *(str + len) );
    *(str + len) = temp;
  }
  printf("Reverse & lower: %s\n", str);
}
