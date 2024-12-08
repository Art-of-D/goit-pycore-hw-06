def caching_fibonacci(n, cache):
  if n in cache:
    return cache[n]
  else:
    result = caching_fibonacci(n - 1, cache) + caching_fibonacci(n - 2, cache)
    cache[n] = result
    return result
  
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
