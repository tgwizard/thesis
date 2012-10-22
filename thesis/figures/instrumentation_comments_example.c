void swap(int *x, int *y)
  /*@
      assume x && y && x != y;
      promise *x == in *y;
      promise *y == in *x;
  @*/
{
  *x = *x ^ *y;
  *y = *x ^ *y;
  /*@
      assume *y == in *x;
  @*/
  *x = *x ^ *y;
}
