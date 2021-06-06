def recursive_power(num, power=0, current_result=1):
    if power == 0:
        print(current_result)
        return
    for _ in range(power):
        current_result *= num
        recursive_power(num, power-1, current_result)



print(recursive_power(2, 10))
print(recursive_power(10, 100))
