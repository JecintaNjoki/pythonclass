def year_of_birth(name,age):
    year=2023-age
    print(f"Hello{name},you were born in {year}")
def my_country(country="Kenya"):
        print(f"Hello you are from{country}")  
def hello(*names):
    for name in names:
        print(f"Hello{name}") 

def sum(*nums):
    answer=0
    for num in nums:
        answer+=num
        return answer 
    
def multiply_many(**kwargs):
    answer=1
    for num in kwargs.values():
      answer*=num

    return answer
   
def concatenate_args(*names):
    answer=""
    for name in names:
      answer+=name
    return answer
    
def concatenate_kwargs(**kwargs):
    answer=""
    for arg in kwargs.values():
        answer+= arg
    return answer
def name(student,school): 
    return(f"I am {student} in {school}")
print()
print(name(school="Akirachix",student="Jecinta"))

def sum_multiplication(sum,multiplication):
    return(f"The sum of 6 and 2 is {sum} and their product is {multiplication}")
print(sum_multiplication(8,2))

def names(firstname="a",secondname="b"):
    return(f"my name is {firstname} {secondname}")
print(names())
print(names("Jecinta"))
print(names("Jecinta","Njoki"))
print(names(firstname="Jecinta")) 
print (names(firstname="Jecinta",secondname="Kimani"))  
         
# args-positional args
def firstname(*names):
    for name in names:
        print(f"hello {name}")
        print(f"hello {final}")
    # final=[name for name in names]
    # print(f"hello {final}")
    firstname("Barnabas","Sam","Ann","Margaret","Samson","Florence","Isaac")
#     #  kwargs
def firstname(**names):
    result=""
    for name in names.values():
        result*=append(name)
        return name    
        

