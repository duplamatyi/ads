#include "fibo.h"

int fibonacci(int n, int f1, int f0) {
  // Tail call recursive Fibonacci
  if (n == 0) {
    return f0;
  }

  if (n == 1) {
    return f1;
  }

  return fibonacci(n - 1, f1 + f0, f1);
}
