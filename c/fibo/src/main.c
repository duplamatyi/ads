#include <stdio.h>
#include "fibo.h"

int main(int argc, char** argv) {
  int a;
  a = fibonacci(0, 1, 1);
  printf("The result is: %i.\n", a);
  a = fibonacci(1, 1, 1);
  printf("The result is: %i.\n", a);
  a = fibonacci(2, 1, 1);
  printf("The result is: %i.\n", a);
  a = fibonacci(10, 1, 1);
  printf("The result is: %i.\n", a);

  return 0;
}
