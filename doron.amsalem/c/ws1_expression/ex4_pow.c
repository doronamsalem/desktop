/* return 10 in power of n */
double mypow(int n)
{
double sum=1.0;
if ( n < 0)
  for(int i = 0; i > n; i--)
	sum *= (1 / 10.0);
else
  for(int i = 0; i < n; i++)
	sum *= 10;
	
return sum;
}


