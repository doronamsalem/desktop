void swapValue( int *num1, int *num2)
{
int holder;
holder = *num2;
*num2 = *num1;
*num1 = holder;
}
/*why pointer as a holder doesn't work( int *holder) */
