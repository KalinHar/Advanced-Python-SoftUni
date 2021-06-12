from modules.math_operations.constants import operation_mapper

num_1, sign, num_2 = input().split(" ")
num_1, num_2 = float(num_1), float(num_2)

result = operation_mapper[sign](num_1, num_2)

print(f"{result:.02f}" if type(result) == float else result)
