clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
number_of_racks = 1
rack_quantity = 0

while clothes:
    if clothes[-1] <= rack_capacity - rack_quantity:
        rack_quantity += clothes.pop()
    else:
        number_of_racks += 1
        rack_quantity = 0

print(number_of_racks)
