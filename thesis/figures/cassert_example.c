#include <assert.h>
#include <stdlib.h>

char *alloc_and_copy(char *src, int n) {
  assert(src != NULL);
  assert(n >= 0);
  char *dst = (char*) malloc(n);
  if (dst == NULL)
    exit(1);
  while (n--)
    dst[n] = src[n];
  return dst;
}

