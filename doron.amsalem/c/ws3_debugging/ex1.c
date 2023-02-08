#include <stdio.h>

void shtut (int f);
int main ()
{
 int arr[] = {0, 1, 2, 3, 4};
 int i = 1;
 for ( ; i < (sizeof(arr)/sizeof(arr[0])) ; ++i )
 {
    if ( arr[i-1] < arr[i] )
    {
	++arr[i - 1];
	shtut(7);
    }
    else
    {
	++arr[i];
    }
 }
 return (0);
}

void shtut(int f)
{
 printf ("prefesional shtutolog");
if (5>2)
printf("a");
else
printf("b");

while(f > 4)
f--;
}
