#Task 1
def print_text():
...     print('"Don\'t compare yourself with anyone in this world...\nif you do so, you are insulting yourself."\n\t\t\
... t\t\tBill Gates')
print_text()

#Task 2
def print_even_numbers(start, end):    
    for num in range(start, end + 1):
        if num % 2 == 0:
         print(num)
print_even_numbers()

#Task 4
def find_smallest(a, b, c, d, e): 
   return min(a, b, c, d, e)
find_smallest()

#Task 5
def product_of_range(start, end):
   if start > end:
    start, end = end, start
   return start, end
product_of_range()

#Task 6
def count_digits(number):
   return len(str(abs(number)))
count_digits()

#Task 7
def is_palindrome(number):
   str_number = str(number)
return str_number == str_number[::-1]
is_palindrome()

#Zadanie 1!
def print_sentence_multiple_times(n):
   for _ in range(n):
      print('Hello Python!')
print_sentence_multiple_times()

#Zadanie 2!
def count_upper_lower_chars(input_string):
   uppercase_count = 0
   lowercase_count = 0
   other_count = 0
   for char in input_string:
      if char.isupper():
         uppercase_count += 1
      elif char.islower():
         lowercase_count += 1
      else:
         other_count += 1
return {'uppercase': uppercase_count ,' lowercase': lowercase_count, 'other': other_count}
count_upper_lower_chars()
