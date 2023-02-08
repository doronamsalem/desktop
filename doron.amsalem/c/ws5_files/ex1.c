#include <stdio.h>   /* print() */

void Print(int number);
int main()
{
	struct print_me
	{
	int number;
	void (*printfunc)(int);
	};
	struct print_me arrayprint[10];
	int i = 0;
	for (i = 0; i < 10; i++)
	{
		arrayprint[i].number = i * 2;
		arrayprint[i].printfunc = Print;
	}

	for (i = 0; i < 10; i++)
        {
                arrayprint[i].printfunc(arrayprint[i].number);
        }
}


void Print(int number)
{
	printf (" the number is: %d\n" , number);
}
