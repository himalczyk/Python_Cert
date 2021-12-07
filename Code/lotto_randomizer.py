def my_factorial(n):
    
    factorial = 1
    
    for number in range(2, n+1):
        factorial = factorial*number
        
    return factorial

n = 49
k = 6
win_probability = my_factorial(n) / (my_factorial(6) *my_factorial(n-k))

print(f"The probability of winning is: {1/win_probability:.10f}")