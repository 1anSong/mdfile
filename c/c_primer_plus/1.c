#include <stdio.h>
int main(void) {
  int bph2o = 212;
  int rv;
  int i;
  i = printf("hello%d\n", bph2o);
  printf("%d\n", i);
  rv = printf("%d F is water's boiling point.\n", bph2o);
  printf("The printf() function printed %d characters.\n", rv);
  return 0;
}
