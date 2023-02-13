import random
passlen = int(input('Enter the length of the password: '))
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ01234567890!#$%'
p = ''.join(random.sample(s, passlen)) # sample(sequence, k) Sequence = list, tuples, string or set k = integer value or length of the sample
print(p)