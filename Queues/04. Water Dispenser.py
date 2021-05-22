from collections import deque
END_COMMAND = "End"
START_COMMAND = "Start"
water_quantity = int(input())
people_collection = deque()
while True:
    command = input()
    if command == START_COMMAND:
        break
    else:
        people_collection.append(command)
while True:
    new_command = input()
    if new_command == END_COMMAND:
        break
    else:
        new_command = new_command.split()
        if len(new_command) > 1:
            litters = int(new_command[1])
            water_quantity += litters
        else:
            litters = int(new_command[0])
            person = people_collection.popleft()
            if water_quantity >= litters:
                print(f"{person} got water")
                water_quantity -= litters
            else:
                print(f"{person} must wait")
print(f"{water_quantity} liters left")