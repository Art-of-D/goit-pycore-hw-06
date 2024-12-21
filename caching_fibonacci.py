from typing import Callable

def caching_fibonacci() -> Callable[[], int]:
  """
  Returns a function that calculates the nth Fibonacci number, but caches
  previously calculated numbers to speed up the calculation.

  Need to use through function variable, like fib = caching_fibonacci()
  """
  cache = {}
  def fibonacci(n) -> int:
    if n <= 1:
      return n
    if n in cache:
      return cache[n]
    else:
      result = fibonacci(n - 1) + fibonacci(n - 2)
      cache[n] = result
      return result

  return fibonacci

# Getting the function
fib = caching_fibonacci()

# Using the function
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
