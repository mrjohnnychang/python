#for and append and sort
start_list = [5, 3, 1, 2, 4]
square_list = []
for i in start_list:
  square_list.append(i ** 2)
square_list.sort()
print square_list

#Dictionary:
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin'] # Prints Puffin's room number
print residents['Sloth']
print residents['Burmese Python']
dict_name[key] = new_value
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

#dictionary note 2
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

#dictionary note 3
prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

total = 0

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  print prices[key] * stock[key]
  total = total + prices[key] * stock[key]
  
print total

shopping_list = ["banana", "orange", "apple"]

# Write your code below!
def compute_bill(food):
  total = 0
  for i in food:
    if stock[i] > 0:
      total += prices[i]
      stock[i] -= 1
  return total


#dictionary note4
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = float(sum(numbers)) / len(numbers)
  return total

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"

print get_letter_grade(get_average(lloyd))

def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
  return average(results)

students = [alice, lloyd, tyler]
print get_class_average(students)

n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]

n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]

del(n[1])
# Doesn't return anything
print n
# prints [1, 5]

n = "Hello"
# Your function here!
def string_function(s):
  return s + "world"
print string_function(n)

n = [3, 5, 7]
# Add your function here
def list_extender(lst):
  lst.append(9)
  return lst
print list_extender(n)

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x
print my_function(range(3)) # Add your range between the parentheses and print out [0,1,2]

def total(numbers):
  result = 0
  for i in range(len(numbers)):
    result += numbers[i]
  return result
  
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for i in range(len(words)):
    #using += can add letters to strings
    result += words[i]
  return result
print join_strings(n)  

m = [1, 2, 3]
n = [4, 5, 6]
def join_lists(x, y):
  return x + y
print join_lists(m, n)
#print [1, 2, 3, 4, 5, 6]

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
  results = []
  for numbers in lists:
    for i in numbers:
      results.append(i)
  return results

print flatten(n)
#prints [1,2,3,4,5,6,7,8,9]


#number guessing game:
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
  guess = int(raw_input("Your guess: "))
  guesses_left -= 1
  if guess == random_number:
    print "You win!"
    break
    pass
else:
  print "You lose."
  
  
#loop note1
  hobbies = []

# Add your code below!
for i in range (3):
  hobby = str(raw_input("What is your hobby? "))
  hobbies.append(hobby)
print hobbies

#loop note 2, print dictionary key and value
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
  # Your code here!
  print key, d[key]

#enumerate note
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
  print index+1, item

#zip note, zip creates a pair of elements when passing 2 or more lists
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print a
    pass
  else:
    print b

#calculate sum of digits
def digit_sum(n):
  x= 0
  y = 0
  while n > 9:
    x = n % 10
    y = x + y
    n = n // 10
  else:
    y = y + n
  return y

print digit_sum(4444)


  
#calculate factorial
def factorial(x):
  y = 1
  while x > 1:
    y = x * y
    x -= 1
  else:
    return y
  return y

print factorial(0)

#prime number checker:
def is_prime(x):
  if x < 2:
    return False
  elif x == 2:
    return True
  elif x == 3:
    return True
  else:
    for n in range(2, x-1):
      if x % n == 0:
        return False
    return True
  
  
#reverse a word
def reverse(text):
  a = []
  for i in range(0, len(text)):
    a.append(text[len(text) - (i + 1)])
  return "".join(a)

print reverse("pearl")
