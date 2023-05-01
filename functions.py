#Define a function that accepts a string as input and uses the
# for loop to iterate  through the string and count the vowels
def count_vowels(name):
    count=0
    vowels=("a","e","i","o","u")
    for i in name:
     for v in vowels:
         if i==v:
          count+=1
         return count

         print(count_vowels())

def count_vowels(school):
    count=0
    vowels='a','e','i','o','u'
    for char in school:
       if char in vowels:
         count+=1
    return count

school ="Akirachix"
my_vowel=count_vowels(school)
print(my_vowel) 


# Write a Python function that takes two arguments (a and b) 
# and returns their sum.
def add_numbers(a,b):
   sum=0
   for num in a,b:
      y=a+b
print(add_numbers([38,52]))   

 


   

# Write a Python function that takes a string as input and 
# returns the string reversed.
def reverse_string(names):
    string = ""
    for i in names:
        string = i + string
    return string
print(reverse_string("magenta"))
 
 
      



# Write a Python function that takes a list of integers 
# as input and returns the sum of all the integers in the list.
def list_of_integers(nums):
   sum=0
   for i in nums:
      sum=sum+1
      return sum
print(list_of_integers([10,20,30,40,50]))   
   

# Write a Python function that takes a list of integers as # input and returns a new list with all the even numbers removed.
def   list_of_numbers(nums):
      x=0
      for i in nums:
        if x % 2==0:
          evenlist.remove(x)
        print(evenlist)
        evenlist=[2,3,7,6,15,22,36,27,30]



# Write a Python function that takes a list of integers as 
# input and returns the highest value in the list.
def highest_of_integers(numbers):
    highest=0
    highest.max=numbers
    return highest
print(highest_of_integers([99,54,37,23,73]))

# Write a Python function that takes a list of strings as input
#  and returns a new list with all the strings capitalized.
def list_of_strings(names):
   capitalized=names.uppercase
   return capitalized
print (list_of_strings("amazing grace"))
    
