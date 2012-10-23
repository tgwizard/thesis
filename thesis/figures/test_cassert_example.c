#include <stdio.h>
#include "cassert_example.c"

int main(int argc, char **argv) {
  char *s = "this is an example sentence";

  char *t = alloc_and_copy(s, 7);
  printf("%s\n", t);
  return 0;
}
