from typing import Callable

def caching_fibonacci() -> Callable[[], int]:
  """
  Returns a function that calculates the nth Fibonacci number, but caches
  previously calculated numbers to speed up the calculation.
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

fib = caching_fibonacci()

print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
