lower = 100
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")
def getPrime(lower,upper):
    for num in range(lower, upper + 1):
      if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

getPrime(lower,upper)