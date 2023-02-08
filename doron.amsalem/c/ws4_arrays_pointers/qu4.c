#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void PrintArray (char **array);
void CopyArray (char **envp, char **newenvp);
int NumOfElements ( char **envp );
void LowerVars ( char **newarr);

int main(int argc, char **argv, char **envp)
{
	char **newenvp = (char **)malloc(sizeof(char *) * NumOfElements(envp) );
	if (newenvp == NULL)
	{
		printf("allocation failed");
	}

	else
	{
		CopyArray(envp, newenvp);
		LowerVars ( newenvp );
		PrintArray(newenvp);
	}
	return (0);

        /*      char *temp;
                for (i = 0; *(envp + i) != NULL; ++i )
                {
                        for ( x = 0; **(envp + x) != '\0'; x++ );
										//should allocate place for each 
                        temp = (char *)malloc(x);                               //pointer and insert new pointer each time to newenv
                        CopyArray(envp, newenvp, temp);
                }
        */
}


void CopyArray (char **envp, char **newenvp)
{
	int i = 0;
        for (i = 0; *(envp + i) != NULL; ++i )
	{
		*(newenvp + i) = *(envp + i);
	}
	*(newenvp + i) = *(envp + i);    /* insert last null pointer */
}


int NumOfElements ( char **envp )
{
	int i = 0;
	for (i = 0; *(envp + i) != NULL; ++i );
	return (i + 1); 	/* number of elements + null */
}


void PrintArray (char **array)
{
	int i = 0;
       for (i = 0; *(array + i) != NULL; ++i )
       {
		printf("%s\n", *(array + i) );
       }
}

void LowerVars ( char **newarr)
{
	int i =0, x = 0;
	char *temp ;
        for (i = 0; *(newarr + i) != NULL; ++i )
	{
		temp = *(newarr + i);
        	for ( x = 0; *(temp + x) != '\0'; x++ )
		{
			if (*(temp + x) > 'A' && *(temp + x) < 'Z' )
			{
				*(temp + x) = *(temp + x) + 32;
			}
		}

	}
}
