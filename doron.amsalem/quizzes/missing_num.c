#include <stdio.h>

int MissingNum (int *arr, int size)
{
	int sum = 0, sum_index = 0, i = 0;
	for (i = 0; i < size; i++)
	{
		sum += *(arr + i);
		sum_index += i;
	}
	sum_index += i;
	return (sum_index - sum);
}

int main()
{
	int arr[] = {2, 3, 4, 1, 5};
	printf("the missing number is: %d\n", MissingNum(arr, 5) );
	return 0;
}
