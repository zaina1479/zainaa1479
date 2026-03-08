# fizz اذا يقبل القسمة على 3
# buzz اذا يقبل القسمةعلى 5
# fizzbuzz اذا يقبل القسمة على كليهما

for i in range(1, 101):
  if i % 3 == 0:
   print ("Fizz")  
  elif i % 5 == 0:
   print("Buzz")
  elif i % 3 == 0 and i % 5 == 0:
   print("FizzBuzz")
  else :
   print ("erorr")
