n = int(input("Check this number: "))

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0: # If this is false, the prime number will remain True because prime numbers can only be divided by 1 and themselves. If not then it will became false
      is_prime = False # Because there are many factor that can be divided by number
  if is_prime: # is_prime == True
    print("It's a prime number")
  else: # is_prime == False 
      print("It's not a prime number")
  
prime_checker(number=n)
