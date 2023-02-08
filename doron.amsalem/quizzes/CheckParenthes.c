#include "stdio.h"
#include <stdlib.h>
int MatchCloser ( char opener, char closer );
int CheckParentheses (char *str);

int main ()
{
        char str[80];
	printf("enter your string for checking\n");
	scanf("%s", str);
        if (CheckParentheses(str) == 0 )
                printf("patern corect\n");
        else
                printf("patern wrong\n");
        return 0;
}


int CheckParentheses (char *str)
{

	int i = 0, index = 0;
	size_t str_capacity = 0;
	char *opens_arr = NULL;
	for (i = 0; str[i] != '\0'; i++)
	{
		str_capacity += sizeof(str[i]);
	}

	opens_arr = (char *)malloc(str_capacity);
	if ( opens_arr == NULL)
	{
		printf("allocation failed\n");
		return 1;
	}
	else
	{
		for (i = 0; str[i] != '\0'; i++)
		{
			if ( str[i] == '(' || str[i] == '{' || str[i] == '[' )
			{
				opens_arr[index] = str[i];
				index++;
			}
			else if ( str[i] == ')' || str[i] == '}' || str[i] == ']' )
			{
				if ( MatchCloser(opens_arr[index - 1], *(str + i) ) != 0)
				{
					return 1;
				}
				else
				{
					index--;
				}
			}
		}
		if ( index == 0 )
		{
			return 0;
		}
		else
		{
			return 1;
		}
	}
	free(opens_arr);
}

int MatchCloser ( char opener, char closer )
{
	if ( closer == ')' )
	{
		if ( opener == '(' )
			return 0;
	}
	else if ( closer == ']' )
	{
                if ( opener == '[' )
                        return 0;
        }
        else if ( closer == '}' )
        {
                if ( opener == '{' )
                        return 0;
        }
	else
		return 1;
}

