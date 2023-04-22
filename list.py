names=["Mercy","Nancy","Regina","Susan","Marion","Ann","Lekishon",45,True]
first,second,third,*rest=names
print(first)
print(second)
print(third)
print(*rest)
#sort
numbers=[23,45,67,89,12,56]
numbers.sort()
print(numbers)
#reverse
numbers.reverse()
print(numbers)

numbers.sort(reverse=True)
print(numbers)
#range
name2=range(numbers[0],numbers[-3])
print(numbers)
mylist=[*range(10,20)]
print(mylist)

print(numbers)
 # append
cars=["subaru","jeep","toyota","mercedez"]
cars.append("audi")
print(cars)

#copy
months=["january","september","july","may"]
months.copy()
print(months)

#extend
ages=[8,22,15,55,33]
time=[10 ,12,7,4]
ages.extend (time)
print(ages)





