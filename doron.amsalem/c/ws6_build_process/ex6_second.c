
int StrCmp(const char *s1, const char *s2)
{
 int diff = 0, i = 0;
 while ( !diff )
 {
   diff = (int)*(s1 + i) - (int)*(s2 + i);
   if ( *(s1 + i) == '\0' || *(s2 + i) == '\0' )
   {
     break;
   }
   ++i;
 }
 return diff;
}
