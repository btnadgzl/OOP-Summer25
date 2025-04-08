#Create a variable
x= "Batın"
y = 2005
print(x)
print(y)

#Variable names 
my_var = "Batın"
print(my_var)

#Assign multiple values
x,y,z = ("volvo","audi","honda")
print(x)
print(y)
print(z)

#Unpack a collection
carsmodels = ["s90","rs6","typeR"]
x, y, z = carsmodels
print(x)
print(y)
print(z)

#Create a dict
my_dict = {
  "brand": "Honda",
  "model": "Civic",
  "year": 2020
}
print(my_dict)
#Change Dictionary Items
my_dict = {
  "brand": "Honda",
  "model": "Civic",
  "year": 2020
}
my_dict["year"] = 2018

#Strings
print("Hello")
print('Hello')

#Create a list
my_list = ["headphone", "keyboard", "motherboard"]
print(my_list)

#If ... Else
a = 89
b = 314
if b > a:
  print("b is greater than a")

#Create a Class
class MyClass:
  x = 12
  print(MyClass)
