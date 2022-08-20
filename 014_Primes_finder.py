#version_1
n = 20
number_range = set(range(2, n+1))
primes_list = []

prime = number_range.pop()
primes_list.append(prime)
multiples = set(range(prime*2, n+1, prime))
number_range.difference_update(multiples)
#version_2
n=1000
#number_range = set(range(2, n+1))
#empty list to append discovered primes to
primes_list = []
#while loop
while number_range:
  prime = number_range.pop()
  primes_list.append(prime)
  multiples = set(range(prime*2, n+1, prime))
  number_range.difference_update(multiples) 
  
# print our list of primes
print(primes_list)

#number of primes tha#upper bound were found
prime_count = len(primes_list)


#largest_prime 
largest_primes = max(primes_list)
#summary
print(f"There are {prime_count} prime number between 2 and {n}, the largest of which is largest")


#version_3
def primes_finder(n):
    #number_range to be checked
     number_range = set(range(2, n+1))
    
     #empty list to append discovered primes to
     primes_list = []
     #while loop
     while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples) 
  
     #print our list of primes
     print(primes_list)

     #number of primes that were found
     prime_count = len(primes_list)
     
     #largest_prime 
     largest_primes = max(primes_list)
     #summary
     print(f"There are {prime_count} prime number between 2 and {n}, the largest of which is largest_prime")
#version_3


def primes_finder(n):
    
    #number_range to be checked
     number_range = set(range(2, n+1))
    
     #empty list to append discovered primes to
     primes_list = []
     #while loop
     while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        multiples = set(range(prime*2, n+1, prime))
        number_range.difference_update(multiples) 
  
     #print our list of primes
     print(primes_list)

     #number of primes that were found
     prime_count = len(primes_list)
     
     #largest_prime 
     largest_primes = max(primes_list)
     #summary
     print(f"There are {prime_count} prime number between 2 and {n}, the largest of which is largest_prime")
     
     return primes_list

primes_finder(100)
primes_list = primes_finder(100)
print(primes_list)

primes_list= primes_finder(1000000)
    

