#include <stdio.h>

int IsSumFound (int *arr, int sum, int len, int *result)
{
	int first = 0, last = (len - 1);
	while ( first < last )
	{
		if ( *(arr + first) + *(arr + last) > sum )
		{
			--last;
		}
                else if ( *(arr + first) + *(arr + last) < sum )
                {
                        ++first;
                }
		else
		{
			result[0] = first;
                        result[1] = last;
			return 1;
		}
	}
        result[0] = first;
        result[1] = last;
        return 0;
}


int main()
{
	int arr[7]= {1, 3, 5, 12, 31, 34, 35}, sum = 0, result[2] = {0,0};
	printf ("please enter sum: ");
	scanf("%d", &sum);
	if ( IsSumFound ( arr, sum, sizeof(arr) / sizeof(arr[0]), result ) == 1  )
	{
		printf("the element's indexs that equal to sum(%d) are: %d  %d\n", sum, result[0], result[1] );
	}
	else
	{
		printf("there aren't element that equal to sum(%d)\n", sum);
	}
	return 0;
}

