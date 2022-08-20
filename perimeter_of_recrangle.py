 # Fibonacci sequence square perimeter calculating functiom

def perimeter(n):
    numbers = [1, 1]
    num = 0
    for i in range(n - 1):
        if n > 1:
            num = numbers[len(numbers) - 1] + numbers[i]
        else:
             pass
        numbers.append(num)
    result = 4 * sum(numbers)
    return result


        
perimeter(20)