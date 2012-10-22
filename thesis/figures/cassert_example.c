#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

void bad_strcpy(char *dst, char *src) {
  assert(dst != NULL);
  assert(src != NULL);
  while (*dst++ = *src++) {}
}

int main(int argc, char **argv) {
  char *s = "this is an example sentence";
  char *t = (char*) malloc(1000);
  if (t == NULL)
    exit(1);

  bad_strcpy(t, s);
  printf("%s\n", t);
  return 0;
}
