#include <stdio.h>
void BitSort (int *arr, size_t len)
{
	size_t last_0 = 0, i = 0;
	int temp = 3;
	for ( i = 0 ; i < len; i++)
	{
		if ( *(arr + i) == 0 )
		{
			temp = *(arr + last_0);
			*(arr + last_0) = *(arr + i);
			*(arr + i) = temp;
			last_0++;
		}
	}
}

int main()
{
	int arr[] = {1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0};
	size_t i = 0, len = sizeof(arr) / sizeof(arr[0]);
	BitSort(arr, len);

	for ( i = 0; i < len; i++)
	{
		printf( "%d  ", arr[i] );
	}
	printf("\n");
	return 0;
}
