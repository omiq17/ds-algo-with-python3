# function for fibonacci
def fibonacci(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    else:
        # if the function is called before then returning value from dp list
        if dp[n] != 0:
            return dp[n]
        else:
            # otherwise, saving returned value in dp list for future usage
            dp[n] = fibonacci(n-1) + fibonacci(n-2)
            return dp[n]

# for taking unlimited input
while True:
    n = int(input())
    # taking a list for saving values
    dp = [0] * (n+1)
    result = fibonacci(n)
    print("The " + str(n) + "th Fibonacci number is: " + str(result))
