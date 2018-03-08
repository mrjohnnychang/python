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


