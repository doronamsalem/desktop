/* get number and flip the digits */ 
unsigned flipNum (unsigned num)
{
  int decimalBace=1;
  unsigned fliped=0;
  for(int i=1; (num / decimalBace) > 10; i++) 
       decimalBace = mypow(i);  /* 10^i */
   
  while(decimalBace != 0) 
  {
  
    fliped += (num % 10 * decimalBace);
    num /= 10;
    decimalBace /= 10;
  }   
  return fliped;
}
