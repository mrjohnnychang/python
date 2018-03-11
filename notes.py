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


#anti-vowel
def anti_vowel(text):
  a = []
  for i in range(0, len(text)):
    if text[i] != "a" and text[i] != "e" and text[i] != "i" and text[i] != "o" and text[i] != "u" and text[i] != "A" and text[i] != "E" and text[i] != "I" and text[i] != "O" and text[i] != "U":
      a.append(text[i])
      pass
  return "".join(a)

print anti_vowel("pearl")


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  x= 0
  for i in word:
    print i
    print score[i]
    #score[i] is the int score for the letter.  e.g. in "pearl", p has score 3,  i = p and hence score[p] is 3
    #add the score to x (total)
    x += score[i]
    print x
  return x
#testing
print scrabble_score("pearl")


#censor text with word
def censor(text, word):
  #star = * times number of letters in word
  star = "*" * len(word)
  #.split() separates the words in a string. e.g. "the day" becomes ['the', 'day']
  split = text.split()
  for i in range(len(split)):
    #i is the index: 0,1,2,3
    #split[i] is the separated words: the, day
    #checks if split[i] matches the word to censor
    if split[i] == word:
      #if matches, replaces word with stars
      split[i] = star
      pass
  #joins separated words so it becomes a string
  return " ".join(split)

print censor("the day is fine", "fine")


#count number of times a number show up in a list
def count(sequence, item):
  x = 0
  for i in sequence:
    if item == i:
      x += 1
      pass
  return x
#test
print count([1, 2, 1, 1], 1)


#purifies all odd number out of a list
def purify(x):
  a = []
  for i in x:
    if i % 2 == 0:
      a.append(i)
  return a
#test
print purify([1,2,3])

#multiple all numbers in a list, use range(len(x)) because it is a list
def product(x):
  y = 1
  for i in range(len(x)):
    y = x[i] * y
  return y
#test
print product([4,5,5])


#remove duplicates in a list
def remove_duplicates(l):
  a = []
  for i in range(len(l)):
    if l[i] not in a:
      a.append(l[i])
  return a
#test
print remove_duplicates([1, 1, 2, 2])


#def median(l):
  l = sorted(l)
  if len(l) % 2 != 0:
    return l[len(l)/2]
  else:
    return (l[len(l)/2] + l[((len(l)-1)/2)]) / 2.0
#test
print median([7, 3, 1, 4])


#calcualte average:
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print "This is all the grades: "
def print_grades(grades_input):
  for grade in grades_input:
    print grade
print_grades(grades)
    
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
print "The sum is: ", grades_sum(grades)

def grades_average(grades_input):
  return (grades_sum(grades_input) / float(len(grades_input)))
print "The average is: ", grades_average(grades)

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for i in scores:
    #computes squared difference
    variance = variance + ((average - i) ** 2)
  return (variance / float(len(scores)))
print "The variance is: ", grades_variance(grades)

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)
print "The standard deviation is: ", grades_std_deviation(variance)


#dictionary note5
my_dict = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
#returns array in dictionary
print my_dict.items()
#return keys in dictionary
print my_dict.keys()
#return values in dictionary
print my_dict.values()

for key in my_dict:
  print key, my_dict[key]
  
  
#print only even numbers (0-50)
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50


#lists note1
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# hint: range(1,6) is a list of 1,2,3,4,5
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print "even_squares: ", even_squares
cubes_by_four = [x ** 3 for x in range(1, 11) if (x**3) % 4 == 0]
print cubes_by_four

#lists note2
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#[start:end:stride(steps)]
print l[2:9:2]
#prints [9, 25, 49, 81]

#lists note3
#list of 1 to 21
to_21 = [x for x in range(1,22)]
#just the odds between 1 to 21
odds = to_21[::2]
#middle_third equals to 8 to 14
middle_third = to_21[7:14]

#lambda note
my_list = range(16)
filter(lambda x: x % 3 == 0, my_list)

languages = ["HTML", "JavaScript", "Python", "Ruby"]
# Add arguments to the filter()
print filter(lambda x: x == "Python", languages)

squares = [x ** 2 for x in range(1, 11)]
#prints 36,49,64
print filter(lambda x: x >= 30 and x <= 70, squares)

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message


#bitwise
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT

#check if bit4 is on (1)
def check_bit4(input):
  bitfour = 0b1000
  if (bitfour & input) > 0:
    return "on"
  else:
    return "off"
  
#turn 3rd bit on
a = 0b10111011
third = 0b100
print bin(a | third)

#flip all bits
a = 0b11101110
flipbit = 0b11111111
print bin(a ^ flipbit)

#flip the n bit
def flip_bit(number, n):
  #flip the n bit
  nmask = (0b1 << n-1)
  result = (number ^ nmask)
  return bin(result)


#class, method (__init__) and member variables (is_alive)
class Animal(object):
  """Makes cute animals."""
  #member variable is_alive
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive



#method (description), instance (Animal("hippo", 8))
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age

hippo = Animal("hippo", 8)
hippo.description()

sloth = Animal("sloth", 9)
ocelot = Animal("ocelot", 10)

print hippo.health
print sloth.health
print ocelot.health


#shopping cart
class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  items_in_cart = {}
  def __init__(self, customer_name):
    self.customer_name = customer_name

  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."

#ShoppingCart class has __init__() that takes a customer name
my_cart = ShoppingCart("Name")
my_cart.add_item("Pizza", 8)


#inherited class
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

#Triangle is the new class, Shape is the class which Triangle inherits
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3
    
    
 
