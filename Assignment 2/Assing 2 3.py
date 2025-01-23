import random
li=[random.randint(100,900) for i in range(100)]
#1

odd_numbers = [num for num in li if num % 2 == 1]
print('Odd Numbers= ',odd_numbers)
print('\n')

#2

even_numbers = [num for num in li if num % 2 == 0]
print('Even Numbers= ',even_numbers)
print('\n')

#3

prime_numbers=[]
for num in li:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_numbers.append(num)
print('Prime Numbers= ',prime_numbers)
print('\n')
