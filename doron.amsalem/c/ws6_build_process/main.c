#include <stdio.h>
#include "g.h"

int main()
{
	printf("the value of g_s is: %d\n",g_s);
	Foo();
	printf("the value of g_s after Foo() is: %d\n", g_s);
	return 0;
}

