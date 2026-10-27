def sum_prime():
    the_check = input("Input the number: ")
    
    if the_check.isdigit():
        limit = int(the_check)
        total_sum = 0
        
        for num in range(2, limit + 1):
            is_prime = True
            
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break 
            
            if is_prime:
                total_sum += num
                
        print(f"The sum of primes {limit} is: {total_sum}")
    else:
        print("Please enter a valid positive integer.")

sum_prime()




def sum_prime():
    the_check = input("Input the number: ")
    
    if the_check.isdigit():
        limit = int(the_check)
        total_sum = 0
        
        num = 2
        while num <= limit:
            is_prime = True
            
            i = 2
            inner_limit = int(num ** 0.5)
            while i <= inner_limit:
                if num % i == 0:
                    is_prime = False
                    break 
                i += 1 
            
            if is_prime:
                total_sum += num
                
            num += 1  
                
        print(f"The sum of primes up to {limit} is: {total_sum}")
    else:
        print("Please enter a valid positive integer.")

sum_prime()

