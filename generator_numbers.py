from decimal import Decimal

def generator_numbers(text):
  """
  Extracts numbers from a given text and yields them as Decimal objects.

  Args:
      text (str): The input string containing numbers and other text.

  Yields:
      Decimal: Each number found in the text, converted to a Decimal object.

  Raises:
      ValueError: If the conversion of a word to a float fails.
  """

  if not text:
      return
  list = text.split()
  for word in list:
      try:
          float(word)
          num = Decimal(word)
          yield num
      except ValueError:
          continue

def sum_profit(text, generator_numbers):
  """
  Sums all the numbers in a given text.

  Args:
      text (str): The input string containing numbers and other text.
      generator_numbers (function): A generator of Decimal objects from a given text.

  Returns:
      Decimal: The sum of all the numbers in the text.
  """
  total = Decimal(0)
  for num in generator_numbers(text):
    total += Decimal(num)
  return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
