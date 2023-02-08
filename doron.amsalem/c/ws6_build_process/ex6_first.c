#include <stddef.h>  /*include size_t , sizeof*/
size_t StrLen (const char *s)
{
 size_t bytes = 0;
 int i;
 for ( i = 0; *(s + i) != '\0'; i++  )
 {
     bytes += sizeof(*(s + i));
 }
 return bytes;
}

