#include <stddef.h>  /* include size_t */
void SwapSize_tRef (size_t *elem1, size_t *elem2) /* swap two size_t elements by ref */
{
 size_t *elem_temp = elem1;
 elem1 = elem2;
 elem2 = elem_temp;
}

