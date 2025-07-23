### PRIME NUMBER CHECKER ###

def check_prime(num):
  num = abs(num)
  if num == 0 or num == 1:
    return f'{num} is neither prime nor composite.'
  elif num == 2:
    return f'{num} is a prime number.'
  else:
    for i in range(2,int(num**0.5)+1):
      if num%i == 0:
        return f'{num} is a non-prime composite number'
    return f'{num} is a prime number.'

while True:
  try:
    number = int(input("Want to check if a number is prime?\nEnter the number: "))
    print(check_prime(number))
    break
  except ValueError:
    print('Please enter a number.')
    continue