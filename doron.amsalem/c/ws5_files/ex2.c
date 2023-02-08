/*
	-program for  making or appening files
	-gets special strings for operations
	-code reviwe: baseer
*/
#include <stdio.h>    /* print(),files functions */
#include <stdlib.h>   /* exit() */
#include <string.h>   /* strcmp() */
/* special functions*/
int CountLines ( const char *file, char *str );
int AppenedBegining ( const char *file, char *str );
int RemoveFile ( const char *file, char *str );
int ExitProg ( const char *file, char *str );

int AppenedEnd ( const char *file, char *str );
int CompareStr( char *str, char *special, int struct_num );

#define MAX_STR_LEN 81
enum returned_val{ failed, success };

int main(int argc, char **argv)
{
    if ( argc <= 1 )
    {
         printf("you must enter file name to the program!\n");
         return failed;
    }
    else
    {
	int struct_ind = 0;
	struct specialoption 			/*struct for special option of input*/
       {
                char * command;
                int (*compare)(char *, char *, int);
                int (*operation)(const char *, char *);
        };
        struct specialoption arraystrc[4]=	     /*all the special options*/
	{
		{ "-remove\n", CompareStr, RemoveFile},
		{"-count\n", CompareStr, CountLines},
		{"-exit\n", CompareStr, ExitProg},
		{"<", CompareStr, AppenedBegining}
	};
	char newstring[MAX_STR_LEN];
	const char *filename = *(argv + 1);

        printf("your special options are:\n\n   \"<\"    (append to the begining)\n\"-remove\" (delete the file)\n\"-count\" (number of lines and characters)\n\"-exit\" (close the progres)\n");
	while( 1 )
	{
		printf("\nplease append string to file(till 80 chars):\n");
		fgets(newstring, MAX_STR_LEN , stdin);

		for ( struct_ind = 0; struct_ind <= 5; struct_ind++ )
		{
			if ( struct_ind  == 4 )           /* non of the special options had writen*/
			{
				AppenedEnd( filename, newstring );
				break;
			}
                        else if ( struct_ind  == 5 )
                        {
                                printf("somting went wronge\n");
                        }
			else if ( arraystrc[struct_ind].compare(newstring, arraystrc[struct_ind].command, struct_ind) )
			{
				arraystrc[struct_ind].operation( filename,newstring );
				break;
			}
		}
	}
    }
	return success;
}
/*check if user entered special command*/
int CompareStr(char *str, char *special, int struct_num )
{
	if ( strcmp(str, special) == 0 )
	{
		return success;
	}
	else if ( struct_num == 3  && *str == *special )
	{
		return success;
	}
	else
	{
		return failed;
	}
}
/*gets file name and return number of  lines in this file*/
int CountLines ( const char *file, char *str)
{
	int count = 0;
	char c = '\0';
	FILE *filename = fopen(file, "a+");
        if (filename == NULL)
        {
                printf("open file failed in CountLines()\n");
        	return failed;
	}
	else
	{
		fseek(filename, 0 , SEEK_SET);
     		for (c = getc(filename); !feof(filename) ; c = getc(filename))
        	{
			if (c == '\n') 		/* count another line */
	      	        count = count + 1;
		}
		printf("you have %d lines and %ld characters in %s\n", count, ftell(filename), file );
	      	return success;
	}
	fclose(filename);
}
/*Appened string to the begining of the file*/
int AppenedBegining ( const char *file, char *str )
{
	FILE *filename = fopen(file, "r");
        FILE *tempfile = fopen(file, "a+");
        if (filename == NULL || tempfile == NULL)
        {
                printf("open file failed in AppenedBegining()\n");
                return failed;
        }
        else
	{
		char tempstr[MAX_STR_LEN];
		fputs( (str + 1), tempfile);   /* without "<" */
		while ( fgets(tempstr , MAX_STR_LEN, filename) )      /* move all source content to a new file */
		{
			fputs ( tempstr, tempfile );
		}

		filename = fopen(file, "w");
                if ( filename == NULL )
		{
			printf("open file for writing failed");
		}
		else
		{
			 while ( fgets(tempstr , MAX_STR_LEN, tempfile) )  /* move back the new file content to the source one*/
                	{
                      		fputs ( tempstr, filename );
                	}
        	}
	 fclose(filename);
         fclose(tempfile);
         printf("the string appended to the begining\n");
         return success;
	}
}
/*Appened string to the end of the file*/
int AppenedEnd ( const char *file, char *str )
{

        FILE *filename = fopen(file, "a+");
        if (filename == NULL)
        {
                printf("open file failed in AppenedEnd()\n");
		return failed;
        }
        else if ( fputs(str, filename) == EOF)       /* the action of appending*/
        {
		printf("appendation to file failed\n");
		fclose(filename);
                return failed;
        }
	else
	{
                printf("the string was appended to the file\n");
                fclose(filename);
		return success;
	}
}
/* delete the file */
int RemoveFile ( const char *file, char *str )
{
        if( remove(file) == 0 )
	{
		printf("%s has been removed\n", file);
		return success;
	}
	else
	{
		printf("removed() failed\n");
		return failed;
	}
}
/* exit from the progres */
int ExitProg ( const char *file, char *str )
{
        exit(0);
	printf("exit() failed\n");
        return failed;
}
