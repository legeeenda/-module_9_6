def all_variants(text):
  """
  Функция-генератор, которая возвращает все подпоследовательности переданной строки 
  в порядке возрастания длины подпоследовательности.

  Args:
    text (str): Входная строка.

  Yields:
    str: Подпоследовательность строки.
  """

  for i in range(len(text)): 
    yield text[i] 
  for length in range(2, len(text) + 1): 
    for i in range(len(text) - length + 1): 
      yield text[i:i + length] 


a = all_variants("abc")
for i in a:
  print(i)
